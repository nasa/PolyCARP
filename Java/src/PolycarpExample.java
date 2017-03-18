/* PolyCARP Example implementation:
 *   - Using Polycarp for geofence containment checks.
 * 
 * Copyright (c) 2011-2016 United States Government as represented by
 * the National Aeronautics and Space Administration.  No copyright
 * is claimed in the United States under Title 17, U.S.Code. All Other
 * Rights Reserved.
 */

import gov.nasa.larcfm.Util.*;
import gov.nasa.larcfm.ACCoRD.*;
import java.util.*;

public class PolycarpExample{
    public static void main(String args[]) {

	System.out.println("##");
	System.out.println("## PolyCARPj@FormalATM"+Constants.version);
	System.out.println("##\n");

	// Position and velocity data for ownship
	Position so = Position.makeLatLonAlt(37.102456,"deg", -76.387094,"deg", 16.4,"ft");	
	Velocity vo = Velocity.makeTrkGsVs(90.0,"deg", 2.5,"kts", 0.0,"fpm");

	// Add geofence
	double floor     = 0;  // 0 m
	double ceiling   = 10; // 10 m

	// Make a geofence with 4 vertices (keep in fence)
	SimplePoly geoPolyLLA1     = new SimplePoly(floor,ceiling);
	geoPolyLLA1.addVertex(Position.makeLatLonAlt(37.102545,"deg",-76.387213,"deg",0,"m"));
	geoPolyLLA1.addVertex(Position.makeLatLonAlt(37.102344,"deg",-76.387163,"deg",0,"m"));
	geoPolyLLA1.addVertex(Position.makeLatLonAlt(37.102351,"deg",-76.386844,"deg",0,"m"));
	geoPolyLLA1.addVertex(Position.makeLatLonAlt(37.102575,"deg",-76.386962,"deg",0,"m"));

	// Polycarp objects for geofence containment detection and recovery point calculation
	CDPolycarp geoPolyCarp    = new CDPolycarp();	
	PolycarpResolution geoRes = new PolycarpResolution();

	// Project geofence vertices to a local euclidean coordinate system to use with polycarp functions
	EuclideanProjection proj  = Projection.createProjection(geoPolyLLA1.getVertex(0));
	Poly3D geoPoly3D1         = geoPolyCarp.makeNicePolygon(geoPolyLLA1.poly3D(proj));
	
	// Check if ownship violates geofence (use definitelyInside(..) or definitelyOutside(..)
	// based on geofence type [ keep in vs keep out] )
	Vect3 so_3 = proj.project(so); // Project ownship position into local euclidean frame
	if (geoPolyCarp.definitelyInside(so_3,geoPoly3D1)) {
	    System.out.println("Definitely inside of keep in fence");
	}
	if (geoPolyCarp.definitelyOutside(so_3,geoPoly3D1)) {
	    System.out.println("Definitely outside of keep in fence");
	}
	
	//Check if ownship is near any edge (nearness is defined based on horizontal and vertical thresholds)
	double hthreshold = 1; // 1 m
	double vthreshold = 1; // 1 m	
	if (geoPolyCarp.nearEdge(so_3,geoPoly3D1,hthreshold,vthreshold)) {
	    System.out.println("Ownship is near geofence edge");

	    // Compute a safe point to goto
	    double BUFF = 0.1; // Buffer used for numerical stability within polycarp
	    Vect2 so_2  = so_3.vect2(); // 2D projection of ownship position

	    List<Vect2> fenceVertices = new ArrayList<Vect2>();
	    for(int i=0;i<4;i++) {
		fenceVertices.add(geoPoly3D1.getVertex(i)); // Euclidean 2D coordinates of fence vertices.
	    }

	    // Compute safe point
	    Vect2 recpoint = geoRes.inside_recovery_point(BUFF,hthreshold,fenceVertices,so_2);

	    // Convert safe point from euclidean coordinates to Lat, Lon and Alt
	    LatLonAlt LLA = proj.inverse(recpoint,so.alt());
	    Position RecoveryPoint = Position.makeLatLonAlt(LLA.latitude(),LLA.longitude(),LLA.altitude());
	    System.out.println(RecoveryPoint.toString());
	}
    }

}
