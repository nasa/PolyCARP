/* 
 * string_util - String utilities available in Java that we want (or
 *               we want an easier interface to) in C++
 *
 * Contact: Jeff Maddalon (j.m.maddalon@nasa.gov), Cesar Munoz, George Hagen
 *
 * Copyright (c) 2011-2017 United States Government as represented by
 * the National Aeronautics and Space Administration.  No copyright
 * is claimed in the United States under Title 17, U.S.Code. All Other
 * Rights Reserved.
 */

#include "string_util.h"
#include "format.h"
#include <string>
#include <vector>
#include <stdexcept>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <regex>


namespace larcfm {
  
  using std::string;
  using std::vector;

    // Same result as Java's str.split("[" + delimiters + "]+"), that is, a split at each run
    // of delimiter characters:
    // - a run of delimiters at the start gives an empty first field;
    // - if str has no delimiter, the result is str alone (also when str is empty);
    // - empty fields at the end are removed.
    vector<string> split(const string& str,const string& delimiters) {
      vector<string> tokens;
      string::size_type start = 0;
      string::size_type pos = str.find_first_of(delimiters, start);
      if (pos == string::npos) {
        tokens.push_back(str);
        return tokens;
      }
      while (pos != string::npos) {
        tokens.push_back(str.substr(start, pos - start));
        start = str.find_first_not_of(delimiters, pos);
        if (start == string::npos) {
          start = str.size();
          break;
        }
        pos = str.find_first_of(delimiters, start);
      }
      tokens.push_back(str.substr(start));
      while (!tokens.empty() && tokens.back().empty()) {
        tokens.pop_back();
      }
      return tokens;
    }
  
    vector<string> split_empty(const string& str,const string& delimiters) {
      vector<string> tokens;
      string::size_type lastPos = 0; //str.find_first_not_of(delimiters, 0);
      string::size_type pos     = str.find_first_of(delimiters, lastPos);
      while (string::npos != pos) {
    	  //fpln(" www "+str.substr(lastPos, pos - lastPos));
    	  if (pos == lastPos) {
    		  tokens.push_back("");
    	  } else {
    	      tokens.push_back(str.substr(lastPos, pos - lastPos));
    	  }
        lastPos = pos+1;
        pos = str.find_first_of(delimiters, lastPos);
      }
      if (lastPos != str.size()) {
    	  tokens.push_back(str.substr(lastPos, str.size() - lastPos));
      }
      if (lastPos == str.size()) {
    	  tokens.push_back("");
      }
      return tokens;
    }


    // Rewrite the anchors of an ECMAScript expression so that they mean what they mean in
    // a Java expression (without MULTILINE):
    // - '$' matches at the end, and also before a line terminator (\n, \r or \r\n) at the end.
    //   Java does not match '$' between the \r and the \n of a final \r\n: endsWithCrLf tells
    //   that the string ends with \r\n, so that the rewrite can leave out that position.
    // - '^' matches only at the start of the whole string. When atStart is false, the search
    //   begins after the start, so '^' must not match: it becomes an expression that never matches.
    // A '^' or '$' after a backslash or in a character class is not an anchor and does not change.
    static string java_anchors(const string& rgx, bool atStart, bool endsWithCrLf) {
    	string out;
    	bool inClass = false;
    	for (string::size_type i = 0; i < rgx.size(); i++) {
    		const char c = rgx[i];
    		if (c == '\\' && i + 1 < rgx.size()) {
    			out += c;
    			out += rgx[++i];
    		} else if (inClass) {
    			out += c;
    			if (c == ']') {
    				inClass = false;
    			}
    		} else if (c == '[') {
    			out += c;
    			inClass = true;
    		} else if (c == '$') {
    			out += endsWithCrLf ? "(?=(?:\\r\\n)?$)" : "(?=[\\n\\r]?$)";
    		} else if (c == '^' && !atStart) {
    			out += "(?!)";
    		} else {
    			out += c;
    		}
    	}
    	return out;
    }

    // Same result as Java's s.split(rgx_str), that is, Pattern.split(s, 0):
    // - each match of the regular expression ends a field;
    // - a zero-width match at the start of s does not give an empty first field;
    // - after a zero-width match, the next search starts one character later;
    // - if nothing matches, the result is s alone (also when s is empty);
    // - empty fields at the end are removed.
    // The regular expression uses the ECMAScript grammar of std::regex. For the
    // expressions that both grammars accept with the same meaning, the fields are
    // the same as in Java. A malformed expression throws std::regex_error, as Java
    // throws PatternSyntaxException.
    vector<string> split_regex(const string& s, const string& rgx_str) {
    	const bool endsWithCrLf = s.size() >= 2 && s.compare(s.size() - 2, 2, "\r\n") == 0;
    	const std::regex rgxAtStart(java_anchors(rgx_str, true, endsWithCrLf)); // for the search from index 0
    	const std::regex rgxLater(java_anchors(rgx_str, false, endsWithCrLf));  // for the searches after index 0
    	vector<string> elems;
    	const string::size_type length = s.size();
    	string::size_type index = 0;          // start of the next field
    	string::size_type prevStart = string::npos; // previous match (none yet)
    	string::size_type prevEnd = 0;
    	for (;;) {
    		string::size_type from = prevEnd;
    		if (from == prevStart) {
    			from++; // the previous match was empty
    		}
    		if (from > length) {
    			break;
    		}
    		std::smatch m;
    		// After index 0, '\b' must see the character before 'from' (match_prev_avail), as in Java.
    		const bool atStart = (from == 0);
    		const std::regex_constants::match_flag_type flags =
    				atStart ? std::regex_constants::match_default : std::regex_constants::match_prev_avail;
    		if (!std::regex_search(s.begin() + from, s.end(), m, atStart ? rgxAtStart : rgxLater, flags)) {
    			break;
    		}
    		const string::size_type mStart = from + m.position(0);
    		const string::size_type mEnd = mStart + m.length(0);
    		prevStart = mStart;
    		prevEnd = mEnd;
    		if (index == 0 && mStart == 0 && mEnd == 0) {
    			continue; // no empty first field for a zero-width match at the start
    		}
    		elems.push_back(s.substr(index, mStart - index));
    		index = mEnd;
    	}
    	if (index == 0) {
    		return vector<string>(1, s);
    	}
    	elems.push_back(s.substr(index));
    	while (!elems.empty() && elems.back().empty()) {
    		elems.pop_back();
    	}
    	return elems;
    }

    string substring(const string& s, int begin, int end){
    	end = (end < (int) s.length()) ? end : s.length();
    	if (begin < end || begin < 0) {
        	return s.substr(begin,end-begin);
    	} else {
    		return "";
    	}
    }

    string substring(const string& s, int begin){
    	return substring(s, begin, s.length());
    }

    void trim(string& s,const string& drop){
      s.erase(s.find_last_not_of(drop)+1);
      s.erase(0,s.find_first_not_of(drop));
    }
  
    std::string trimCopy(const string& s,const string& drop){
    	std::string tmp(s);
    	trim(tmp, drop);
    	return tmp;
    }

  string toLowerCase(const string& strToConvert) {//change each element of the string to lower case
    string nstr;
    nstr.resize(strToConvert.size());

    for(unsigned int i=0;i<strToConvert.size();i++)  {
      nstr[i] = tolower(strToConvert[i]);
    }
    return nstr;  //return the converted string
    
  }
  
  string toUpperCase(const string& strToConvert) {//change each element of the string to upper case
    string nstr;
    nstr.resize(strToConvert.size());

    for(unsigned int i=0;i<strToConvert.size();i++)  {
      nstr[i] = toupper(strToConvert[i]);
    }
    return nstr;  //return the converted string

  }

  bool equals(const string& s1, const string& s2) {
    return (s1.compare(s2) == 0);
  }
  
  bool equalsIgnoreCase(const string& s1, const string& s2) {
    return (toLowerCase(s1).compare(toLowerCase(s2)) == 0);
  }
  
  void replace(std::string& s, char c1, char c2) {
	  std::replace(s.begin(), s.end(), c1, c2);
  }

  bool contains(const std::vector<std::string>& v, const std::string& s) {
	  for(int i = 0; i < (int) v.size(); i++) {
		  if (equals(v[i],s)) return true;
	  }
	  return false;
  }

  bool contains(const std::string& str, const std::string& sub) {
	  return str.find(sub) != string::npos;
  }

  bool startsWith(const std::string& str, const std::string& prefix) {
	  return str.substr(0,prefix.length()).compare(prefix) == 0;
  }

  bool endsWith(const std::string& str, const std::string& suffix) {
	  return suffix.length() <= str.length() && str.substr(str.length() - suffix.length()).compare(suffix) == 0;
  }


  int parseInt(const std::string& str) {
	  //the C++11 version: return std::stoi(str);
	  std::istringstream buffer(str);
	  int value;
	  buffer >> value;
	  return value;
  }

}
