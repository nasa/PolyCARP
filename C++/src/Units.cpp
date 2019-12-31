/*
 * Units.cpp
 *
 * Contact: Jeff Maddalon
 * NASA LaRC
 *
 * Conversion to internal units: meters, kilogrames, seconds, radians, ...
 *
 * Copyright (c) 2011-2017 United States Government as represented by
 * the National Aeronautics and Space Administration.  No copyright
 * is claimed in the United States under Title 17, U.S.Code. All Other
 * Rights Reserved.
 */

#include "Units.h"
#include "Util.h"
#include "Constants.h"
#include "format.h"
#include "string_util.h"
//#include "DebugSupport.h"
#if defined(_MSC_VER)
#include <regex>
#else
#include <regex.h>
#endif
#include <cstdio>
#include <sstream>
#include <string.h>



using namespace larcfm;
using namespace std;

// The functions below use the "construct-on-first-read" pattern, which avoids
// the static initialization fiasco problem.  This problem manifests itself differently
// between g++ and Visual C++, so be careful if you want to "optimize" this section.

static double FormalATM_unspecified() {
	static double ans = 1.0;
	return ans;
}
static double FormalATM_unitless() {
	static double ans = 1.0;
	return ans;
}
static double FormalATM_internal() {
	static double ans = 1.0;
	return ans;
}

static double FormalATM_m() {
	static double ans = 1.0;
	return ans;
}
static double FormalATM_km() {
	static double ans = 1000.0 * FormalATM_m();
	return ans;
}
static double FormalATM_NM() {
	static double ans = 1852.0 * FormalATM_m();
	return ans;
}
static double FormalATM_ft() {
	static double ans = 0.3048 * FormalATM_m();
	return ans;
}
static double FormalATM_mile() {
	static double ans = 5280.0 * FormalATM_ft();
	return ans;
}
static double FormalATM_inch() {
	static double ans = FormalATM_ft() / 12.0;
	return ans;
}
static double FormalATM_yard() {
	static double ans = 3.0 * FormalATM_ft();
	return ans;
}
static double FormalATM_mm() {
	static double ans = 0.001 * FormalATM_m();
	return ans;
}

static double FormalATM_m2() {
	static double ans = FormalATM_m() * FormalATM_m();
	return ans;
}
static double FormalATM_ft2() {
	static double ans = FormalATM_ft() * FormalATM_ft();
	return ans;
}

static double FormalATM_kg() {
	static double ans = 1.0;
	return ans;
}
static double FormalATM_pound_mass() {
	static double ans = 0.45359237 * FormalATM_kg();
	return ans;
}

static double FormalATM_s() {
	static double ans = 1.0;
	return ans;
}
static double FormalATM_min() {
	static double ans = 60.0 * FormalATM_s();
	return ans;
}
static double FormalATM_hour() {
	static double ans = 3600.0 * FormalATM_s();
	return ans;
}
static double FormalATM_day() {
	static double ans = 8640000.0 * FormalATM_s();
	return ans;
}
static double FormalATM_ms() {
	static double ans = 0.001 * FormalATM_s();
	return ans;
}

static double FormalATM_rad() {
	static double ans = 1.0;
	return ans;
}
static double FormalATM_deg() {
	static double ans = M_PI / 180.0;
	return ans;
}

static double FormalATM_radian_per_second() {
	static double ans = FormalATM_rad() / FormalATM_s();
	return ans;
}

static double FormalATM_degree_per_second() {
	static double ans = FormalATM_deg() / FormalATM_s();
	return ans;
}

static double FormalATM_mps() {
	static double ans = 1.0;
	return ans;
}
static double FormalATM_kph() {
	static double ans = FormalATM_km() / FormalATM_hour();
	return ans;
}
static double FormalATM_kn() {
	static double ans = FormalATM_NM() / FormalATM_hour();
	return ans;
}
static double FormalATM_fpm() {
	static double ans = FormalATM_ft() / FormalATM_min();
	return ans;
}
static double FormalATM_mph() {
	static double ans = FormalATM_mile() / FormalATM_hour();
	return ans;
}
static double FormalATM_foot_per_second() {
	static double ans = FormalATM_ft() / FormalATM_s();
	return ans;
}

static double FormalATM_meter_per_second2() {
	static double ans = FormalATM_m() / (FormalATM_s() * FormalATM_s());
	return ans;
}
double larcfm::FormalATM_gn() {
	static double ans = 9.80665 * FormalATM_meter_per_second2();
	return ans;
}
static double FormalATM_foot_per_second2() {
	static double ans = FormalATM_ft() / (FormalATM_s() * FormalATM_s());
	return ans;
}

static double FormalATM_newton() {
	static double ans = FormalATM_kg() * FormalATM_meter_per_second2();
	return ans;
}
static double FormalATM_slug() {
	static double ans = FormalATM_pound_mass() * FormalATM_gn()
							/ FormalATM_foot_per_second2();
	return ans;
}
static double FormalATM_pound_force() {
	static double ans = FormalATM_slug() * FormalATM_foot_per_second2();
	return ans;
}

static double FormalATM_joule() {
	static double ans = FormalATM_newton() * FormalATM_m();
	return ans;
}
static double FormalATM_foot_pound_force() {
	static double ans = FormalATM_ft() * FormalATM_pound_force();
	return ans;
}


static double FormalATM_pascal() {
	static double ans = FormalATM_newton() / (FormalATM_m() * FormalATM_m());
	return ans;
}
double larcfm::FormalATM_P0() {
	static double ans = 101325.0 * FormalATM_pascal();
	return ans;
}
static double FormalATM_atm() {
	static double ans = 1.0 * FormalATM_P0();
	return ans;
}

const double Units::unspecified = Units::getFactor("unspecified");
const double Units::unitless = Units::getFactor("unitless");
const double Units::internal = Units::getFactor("internal");

const double Units::m = Units::getFactor("m");
const double Units::km = Units::getFactor("km");
const double Units::nmi = Units::getFactor("NM");
const double Units::NM = Units::getFactor("NM");
const double Units::ft = Units::getFactor("ft");
const double Units::mm = Units::getFactor("mm");

const double Units::s = Units::getFactor("s");
const double Units::min = Units::getFactor("min");
const double Units::hour = Units::getFactor("hour");
const double Units::day = Units::getFactor("day");
const double Units::ms = Units::getFactor("ms");

const double Units::rad = Units::getFactor("rad");
const double Units::deg = Units::getFactor("deg");

const double Units::kg = Units::getFactor("kg");
const double Units::pound_mass = Units::getFactor("pound_mass");

const double Units::mps = Units::getFactor("mps");
const double Units::meter_per_second = Units::getFactor("meter_per_second");
const double Units::kph = Units::getFactor("kph");
const double Units::knot = Units::getFactor("knot");
const double Units::kn = Units::getFactor("kn");
const double Units::fpm = Units::getFactor("fpm");

const double Units::meter_per_second2 = Units::getFactor("meter_per_second2");
const double Units::gn = FormalATM_gn();
const double Units::G = Units::getFactor("G");

const double Units::newton = Units::getFactor("newton");
const double Units::pascal = Units::getFactor("pascal");

const double Units::P0 = FormalATM_P0();
const double Units::atm = Units::getFactor("atm");

// Converts value canonical units to [symbol] units
double Units::getFactor(const std::string& symbolp) {

	const std::string symbol = Units::canonical(symbolp);

	if (symbol == "m") {
		return FormalATM_m();
	} else if (symbol == "ft") {
		return FormalATM_ft();
	} else if (symbol == "yard") {
		return FormalATM_yard();
	} else if (symbol == "in") {
		return FormalATM_inch();
	} else if (symbol == "km") {
		return FormalATM_km();
	} else if (symbol == "mi") {
		return FormalATM_mile();
	} else if (symbol == "NM") {
		return FormalATM_NM();
	} else if (symbol == "mm") {
		return FormalATM_mm();

	} else if (symbol == "m^2") {
		return FormalATM_m2();
	} else if (symbol == "ft^2") {
		return FormalATM_ft2();

	} else if (symbol == "s") {
		return FormalATM_s();
	} else if (symbol == "min") {
		return FormalATM_min();
	} else if (symbol == "hour") {
		return FormalATM_hour();
	} else if (symbol == "day") {
		return FormalATM_day();
	} else if (symbol == "ms") {
		return FormalATM_ms();

	} else if (symbol == "rad") {
		return FormalATM_rad();
	} else if (symbol == "deg") {
		return FormalATM_deg();
	} else if (symbol == "deg/s") {
		return FormalATM_degree_per_second();
	} else if (symbol == "rad/s") {
		return FormalATM_radian_per_second();

	} else if (symbol == "kg") {
		return FormalATM_kg();
	} else if (symbol == "lbm") {
		return FormalATM_pound_mass();
	} else if (symbol == "slug") {
		return FormalATM_slug();

	} else if (symbol == "km/h") {
		return FormalATM_kph();
	} else if (symbol == "kn") {
		return FormalATM_kn();
	} else if (symbol == "fpm") {
		return FormalATM_fpm();
	} else if (symbol == "ft/s") {
		return FormalATM_foot_per_second();
	} else if (symbol == "mph") {
		return FormalATM_mph();
	} else if (symbol == "m/s") {
		return FormalATM_mps();

	} else if (symbol == "m/s^2") {
		return FormalATM_meter_per_second2();
	} else if (symbol == "G") {
		return FormalATM_gn();
	} else if (symbol == "ft/s^2") {
		return FormalATM_foot_per_second2();

	} else if (symbol == "N") {
		return FormalATM_newton();
	} else if (symbol == "lbf") {
		return FormalATM_pound_force();

	} else if (symbol == "J") {
		return FormalATM_joule();
	} else if (symbol == "ft-lbf") {
		return FormalATM_foot_pound_force();

	} else if (symbol == "atm") {
		return FormalATM_atm();
	} else if (symbol == "Pa") {
		return FormalATM_pascal();

	} else if (symbol == "internal") {
		return FormalATM_internal();
	} else if (symbol == "unspecified") {
		return FormalATM_unspecified();
	} else if (symbol == "unitless") {
		return FormalATM_unitless();
	}
	return 0.0;  // this is a special value that indicates an invalid unit
}

bool Units::isUnit(const std::string& unit) {
	return getFactor(unit) != 0.0;
}

const std::string Units::canonical(const std::string& unit) {
	if (unit == "unspecified")
		return unit;
	if (unit == "unitless" || unit == "none")
		return unit;
	if (unit == "internal")
		return unit;
	if (unit == "m" || unit == "meter" || unit == "metre")
		return "m";
	if (unit == "ft" || unit == "feet" || unit == "foot")
		return "ft";
	if (unit == "km" || unit == "kilometer")
		return "km";
	if (unit == "NM" || unit == "nmi" || unit == "nm"  // Do not add nm, nm means nanometers, not nautical miles
			|| unit == "nautical_mile")
		return "NM";
	if (unit == "mile" || unit == "mi")
		return "mi";
	if (unit == "inch" || unit == "in")
		return "in";
	if (unit == "yard")
		return unit;
	if (unit == "mm" || unit == "millimeter")
		return "mm";

	if (unit == "m^2")
		return unit;
	if (unit == "ft^2")
		return unit;

	if (unit == "s")
		return "s";
	if (unit == "min" || unit == "minute" || unit == "minutes")
		return "min";
	if (unit == "hour" || unit == "h" || unit == "hr")
		return "hour";
	if (unit == "day")
		return "day";
	if (unit == "ms")
		return "ms";

	if (unit == "rad" || unit == "radian")
		return "rad";
	if (unit == "deg" || unit == "degree")
		return "deg";

	if (unit == "deg/s")
		return unit;
	if (unit == "rad/s" || unit == "radian_per_second")
		return "rad/s";

	if (unit == "kg" || unit == "kilogram")
		return "kg";
	if (unit == "lbm" || unit == "pound_mass")
		return "lbm";
	if (unit == "slug")
		return "slug";

	if (unit == "kph" || unit == "km/h" || unit == "kilometer_per_hour" || unit == "kilometre_per_hour")
		return "km/h";
	if (unit == "knot" || unit == "kn" || unit == "kts")
		return "kn";
	if (unit == "fpm" || unit == "ft/min" || unit == "foot/min"
			|| unit == "feet/min")
		return "fpm";
	if (unit == "m/s" || unit == "mps" || unit == "meter_per_second")
		return "m/s";
	if (unit == "ft/s" || unit == "fps" || unit == "foot_per_second" || unit == "feet_per_second")
		return "ft/s";
	if (unit == "mph")
		return "mph";

	if (unit == "m/s^2" || unit == "meter_per_second2")
		return "m/s^2";
	if (unit == "G")
		return "G";
	if (unit == "ft/s^2" || unit == "foot_per_second2")
		return "ft/s^2";

	if (unit == "newton" || unit == "N")
		return "N";
	if (unit == "lbf" || unit == "pound_force")
		return "lbf";

	if (unit == "joule" || unit == "J")
		return "J";
	if (unit == "foot_pound_force" || unit == "ft-lbf")
		return "ft-lbf";

	if (unit == "atm")
		return "atm";
	if (unit == "pascal" || unit == "Pa")
		return "Pa";

	return "UNKNOWN_UNIT_" + unit;

}

bool Units::isCompatible(const std::string& unit1p, const std::string& unit2p) {
	const std::string unit1 = Units::canonical(unit1p);
	const std::string unit2 = Units::canonical(unit2p);
	if (unit1 == "unspecified" || unit2 == "unspecified") {
		return true;
	}

	if (unit1 == "m" || unit1 == "ft" || unit1 == "km" || unit1 == "NM"
			|| unit1 == "mi" || unit1 == "in" || unit1 == "yard" || unit1 == "mm") {
		return unit2 == "m" || unit2 == "ft" || unit2 == "km" || unit2 == "NM"
				|| unit2 == "mi" || unit2 == "in" || unit2 == "yard" || unit2 == "mm";
	} else if (unit1 == "ft^2" || unit1 == "m^2") {
		return unit2 == "ft^2" || unit2 == "m^2";
	} else if (unit1 == "s" || unit1 == "min" || unit1 == "hour" || unit1 == "ms" || unit1 == "day") {
		return unit2 == "s" || unit2 == "min" || unit2 == "hour" || unit2 == "ms" || unit2 == "day";
	} else if (unit1 == "rad" || unit1 == "deg") {
		return unit2 == "rad" || unit2 == "deg";
	} else if (unit1 == "rad/s" || unit1 == "deg/s") {
		return unit2 == "rad/s" || unit2 == "deg/s";
	} else if (unit1 == "kg" || unit1 == "slug" || unit1 == "lbm") {
		return unit2 == "kg" || unit2 == "slug" || unit2 == "lbm";
	} else if (unit1 == "kph" || unit1 == "kn" || unit1 == "fpm"
			|| unit1 == "m/s" || unit1 == "mph" || unit1 == "ft/s") {
		return unit2 == "kph" || unit2 == "kn" || unit2 == "fpm"
				|| unit2 == "m/s" || unit2 == "mph" || unit2 == "ft/s";
	} else if (unit1 == "m/s^2" || unit1 == "G" || unit1 == "ft/s^2") {
		return unit2 == "m/s^2" || unit2 == "G" || unit2 == "ft/s^2";
	} else if (unit1 == "N" || unit1 == "lbf") {
		return unit2 == "N" || unit2 == "lbf";
	} else if (unit1 == "atm" || unit1 == "Pa") {
		return unit2 == "atm" || unit2 == "Pa";
	} else if (unit1 == "unitless" || unit1 == "none") {
		return unit2 == "unitless";
	}
	return false;

}

// Converts value canonical units to [symbol] units
double Units::to(const std::string& symbol, double value) {
	return value / Units::getFactor(symbol);
}

// Converts value canonical units to [symbol] units
double Units::to(const double symbol, const double value) {
	return value / symbol;
}

double Units::from(const std::string& symbol, double value) {
	return Units::getFactor(symbol) * value;
}

double Units::from(const double symbol, const double value) {
	return symbol * value;
}

double Units::fromInternal(const std::string& defaultUnits, const std::string& units, double value) {
	if (units == "unspecified") {
		return from(getFactor(defaultUnits), value);
	} else {
		return value;
	}
}

std::string Units::str(const std::string& symbol, double value) {
	return str(symbol,value,Constants::get_output_precision());
}

std::string Units::strX(const std::string& symbol, double value) {
	std::ostringstream st;
	st << Units::to(symbol, value) << " [" << symbol << "]";
	return st.str();
}

std::string Units::str(const std::string& symbol, double value, int precision) {
	return FmPrecision(to(symbol, value),precision) + " [" + symbol + "]";
}

static void trimBuilder(std::string& sb) {
	char const* delims = " \t\r\n";

	// trim leading whitespace
	std::string::size_type notwhite = sb.find_first_not_of(delims);
	sb.erase(0, notwhite);

	// trim trailing whitespace
	notwhite = sb.find_last_not_of(delims);
	sb.erase(notwhite + 1);
}

std::string Units::cleanOnly(const std::string& unit) {

	std::string sb(unit);
	trimBuilder(sb);

	  int start_idx = sb.find_first_of("[");
	  if (start_idx >= 0) {
		  sb.erase(0,start_idx+1);
	  }
	  int end_idx = sb.find_first_of("]");
	  if (end_idx >= 0) {
		  sb.erase(end_idx);
	  }
	  trimBuilder(sb);

	return sb;
}

std::string Units::clean(const std::string& unit) {
	std::string sb(cleanOnly(unit));

	if (isUnit(sb)) {
		return sb;
	} else {
		return "unspecified";
	}
}

double Units::parse(const std::string& s) {
	return parse(s,0.0);
}

double Units::parse(const string& str, double default_value) {
	  	return parse("internal", str, default_value);
}

double Units::parse(const std::string& defaultUnitsFrom, const std::string& str) {
	  return parse(defaultUnitsFrom, str, 0.0);
  }


#if defined(_MSC_VER)

double getd(string str, double def) {
	std::istringstream stream;
	stream.str(str);
	double d;
	stream >> d;
	if (stream.fail()) {
		return def;
	}
	return d;
}


double Units::parse(const string& defaultUnitsFrom, const std::string& s, double default_value) {
	double ret = 0.0;
	std::smatch m;
	std::regex numre("\\s*([-+0-9\\.]+)\\s*\\[?\\s*([/^_a-zA-Z0-9]*)\\s*\\]?\\s*$"); //(.*)");   We want to add this unicode character \u00B0 (the degree symbol) to the units part
	//Java: Pattern.compile("\\s*([-+0-9\\.]+)\\s*\\[?\\s*([-\\/^_a-zA-Z0-9\\u00B0]*).*");

	std::regex_match(s, m, numre);
	std::smatch group(m);
	if (group.size() > 0) { // should always be two groups if the regex was matched at all!
		std::string m1(group[1]);
		std::string unit = Units::cleanOnly(group[2]);

		// The logic here can be debated.  What should be returned when
		// an invalid value or invalid unit is provided?  If parse("ft", "10 fjkdsj", 5)
		// is called, what should be returned? Units.from("ft", 10) or Units.from("ft", 5)?
		// I chose Units.from("ft", 10) because in the degenerate case of
		// parse("10 jfkdjks", 5)--that is, with an implied default unit of "internal"--
		// returning 10 seems more correct than returning 5.
		//
		//   supplied                returned (aka converted)
		//   value        unit       value          unit
		//   -----        ----       -----          ----
		//   valid        valid      suppliedvalue  suppliedunit
		//   valid        invalid    suppliedvalue  defunit
		//   invalid      valid      defvalue       defunit
		//   invalid      invalid    defvalue       defunit
		//   illformed               defvalue       defunit

		if (Util::is_double(m1)) {
			ret = Util::parse_double(m1));
			if (Units::isUnit(unit)) {
				ret = Units::from(unit, dbl);
			} else {
				ret = Units::from(defaultUnitsFrom, dbl);
			}
		} else {  // no value
			ret = Units::from(defaultUnitsFrom, default_value);
		}

	} else { // no match
		ret = Units::from(defaultUnitsFrom, default_value);
	}

	return ret;
}

std::string Units::parseUnits(const std::string& s) {
	std::string unit = "unspecified";
	std::smatch m;
	std::regex numre("\\s*([-+0-9\\.]+)\\s*\\[?\\s*([/^_a-zA-Z0-9]*)\\s*\\]?\\s*$"); //(.*)");   We want to add this unicode character \u00B0 (the degree symbol) to the units part
	//Java: Pattern.compile("\\s*([-+0-9\\.]+)\\s*\\[?\\s*([-\\/^_a-zA-Z0-9\\u00B0]*).*");
	std::regex_match(s, m, numre);
	std::smatch group(m);
	if (group.size() > 0) {
		unit = Units::clean(group[2]);
	}
	return unit;
}

#else

double Units::parse(const string& defaultUnitsFrom, const std::string& s, double default_value) {
	double ret = Units::from(defaultUnitsFrom,default_value);
	regex_t regex;
	int reti;
	char msgbuf[100];

	/* Compile regular expression, use C regular expression library */
	reti = regcomp(&regex, "^[[:blank:]]*([-+0-9\\.]+)[[:blank:]]*\\[?[[:blank:]]*([-\\/^_a-zA-Z0-9]*).*", REG_EXTENDED); //[[:blank:]]*\\]?(.*)", REG_EXTENDED);
	//Java: Pattern.compile("\\s*([-+0-9\\.]+)\\s*\\[?\\s*([-\\/^_a-zA-Z0-9\\u00B0]*).*");
	if (reti != 0) {
		fdln("Could not compile regex\n");
		//		DebugSupport::halt();
	}

	/* Execute regular expression */
	regmatch_t matchptr[4];
	reti = regexec(&regex, s.c_str(), 4, matchptr, 0);
	if (!reti) {
		char match[100];
		int numchars;

		// Match #1
		numchars = (int)matchptr[1].rm_eo - (int)matchptr[1].rm_so;
		strncpy(match,s.c_str()+matchptr[1].rm_so,numchars);
		match[numchars] = '\0';
		string m1(match);
		//fpln("match="+m1);

		// Match #2
		numchars = (int)matchptr[2].rm_eo - (int)matchptr[2].rm_so;
		strncpy(match,s.c_str()+matchptr[2].rm_so,numchars);
		match[numchars] = '\0';
		string m2(match);
		//fpln("match2="+m2);
		std::string unit = Units::cleanOnly(m2);
		//fpln("match22="+unit);

		// The logic here can be debated.  What should be returned when
		// an invalid value or invalid unit is provided?  If parse("ft", "10 fjkdsj", 5)
		// is called, what should be returned? Units.from("ft", 10) or Units.from("ft", 5)?
		// I chose Units.from("ft", 10) because in the degenerate case of
		// parse("10 jfkdjks", 5)--that is, with an implied default unit of "internal"--
		// returning 10 seems more correct than returning 5.
		//
		//   supplied                returned (aka converted)
		//   value        unit       value          unit
		//   -----        ----       -----          ----
		//   valid        valid      suppliedvalue  suppliedunit
		//   valid        invalid    suppliedvalue  defunit
		//   invalid      valid      defvalue       defunit
		//   invalid      invalid    defvalue       defunit
		//   illformed               defvalue       defunit

		if (Util::is_double(m1)) {
			double dbl = Util::parse_double(m1);
			if (Units::isUnit(unit)) {
				ret = Units::from(unit, dbl);
			} else {
				ret = Units::from(defaultUnitsFrom, dbl);
			}
		} else {
			//return the default value
		}


		//fpln("ret "+Fm12(ret));
	} else if (reti == REG_NOMATCH) {
		// no match, return default value
	} else {
		regerror(reti, &regex, msgbuf, sizeof(msgbuf));
		string m1(msgbuf);
		fdln("Regex match failed: "+m1);
	}

	/* Free compiled regular expression if you want to use the regex_t again */
	regfree(&regex);
	return ret;
}

std::string Units::parseUnits(const std::string& s) {
	string ret("unspecified");
	regex_t regex;
	int reti;
	char msgbuf[100];

	/* Compile regular expression */
	//reti = regcomp(&regex, "^[[:blank:]]*([-+0-9\\.]+)[[:blank:]]*\\[?[[:blank:]]*([/^_a-zA-Z0-9]*)[[:blank:]]*\\]?(.*)", REG_EXTENDED);
	reti = regcomp(&regex, "^[[:blank:]]*([-+0-9\\.]+)[[:blank:]]*\\[?[[:blank:]]*([-\\/^_a-zA-Z0-9]*).*", REG_EXTENDED); //[[:blank:]]*\\]?(.*)", REG_EXTENDED);
	if (reti != 0) {
		fdln("$$$ERROR$$$: Could not compile regex\n");
//		DebugSupport::halt();
	}

	/* Execute regular expression */
	regmatch_t matchptr[4];
	char match[100];

	//fpln("input X"+s+"X");
	reti = regexec(&regex, s.c_str(), 4, matchptr, 0);
	if (!reti) {
		int numchars;

		// Match #2
		numchars = (int)matchptr[2].rm_eo - (int)matchptr[2].rm_so;
		strncpy(match,s.c_str()+matchptr[2].rm_so,numchars);
		match[numchars] = '\0';
		ret = match;
		ret = Units::clean(ret);
		//fpln("match2 "+ret);
	} else if (reti == REG_NOMATCH) {
		// no match, return default value
	} else {
		regerror(reti, &regex, msgbuf, sizeof(msgbuf));
		fprintf(stderr, "$$$ERROR$$$ Regex match failed line 673: %s\n", msgbuf);
//		DebugSupport::halt();
	}

	/* Free compiled regular expression if you want to use the regex_t again */
	regfree(&regex);
	return ret;
}
#endif
