
# Summary for `PolyCARP`
Run started at 12:44:16 1/21/2026.

_Note_: Time below is expressed in format DD:HH:MM:SS.SSS.

## Grand Totals 

|            | Formulas | Attempted | Succeeded | Missing | Total Time |
| ---:       | :---:    | :---:     | :---:     | :---:   | ---        |
| **totals** | **297**   | **297**    | **297**    | **0**  | **0.450 s**   |
|[top](#top) ✅|0|0|0|0|0.000|
|[edge_proximity](#edge_proximity) ✅|13|13|13|0|0.025|
|[acceptable_polygon](#acceptable_polygon) ✅|54|54|54|0|0.030|
|[good_polygon_def](#good_polygon_def) ✅|6|6|6|0|0.000|
|[in_out_def](#in_out_def) ✅|8|8|8|0|0.001|
|[angle_sum](#angle_sum) ✅|11|11|11|0|0.021|
|[winding_equiv](#winding_equiv) ✅|35|35|35|0|0.128|
|[polygon_contain](#polygon_contain) ✅|23|23|23|0|0.015|
|[detection](#detection) ✅|13|13|13|0|0.068|
|[convex_polygon_containment](#convex_polygon_containment) ✅|36|36|36|0|0.003|
|[convex_polygon_test](#convex_polygon_test) ✅|7|7|7|0|0.002|
|[polygon_containment_test](#polygon_containment_test) ✅|15|15|15|0|0.003|
|[resolution](#resolution) ✅|38|38|38|0|0.056|
|[recurse](#recurse) ✅|2|2|2|0|0.000|
|[time_inout](#time_inout) ✅|26|26|26|0|0.040|
|[multipoly](#multipoly) ✅|10|10|10|0|0.058|

## Detailed Summary 

## `top`
No formula declaration found.
## `edge_proximity`

| Formula | Proof Status | Decision Procedure | Time |
| ---     | ---          | ---                | ---  |
|segment_2Ds_cross_rew1|✅ proved - complete|SHOSTAK|0.000|
|open_segment_2Ds_cross_rew1|✅ proved - complete|SHOSTAK|0.000|
|open_segment_2Ds_cross_rew3_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|open_segment_2Ds_cross_rew3_TCC2|✅ proved - incomplete|SHOSTAK|0.000|
|open_segment_2Ds_cross_rew3|✅ proved - incomplete|SHOSTAK|0.001|
|on_segment_2D_sym|✅ proved - complete|SHOSTAK|0.000|
|near_edge_def|✅ proved - incomplete|SHOSTAK|0.005|
|closest_point_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|closest_point_def|✅ proved - incomplete|SHOSTAK|0.003|
|rev_0_global_min|✅ proved - incomplete|SHOSTAK|0.003|
|segments_2D_close_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|segments_2D_close_TCC2|✅ proved - incomplete|SHOSTAK|0.000|
|segments_2D_close_def|✅ proved - incomplete|SHOSTAK|0.012|

## `acceptable_polygon`

| Formula | Proof Status | Decision Procedure | Time |
| ---     | ---          | ---                | ---  |
|near_poly_edge_TCC1|✅ proved - complete|SHOSTAK|0.000|
|upshot_crosses_edge_TCC1|✅ proved - complete|SHOSTAK|0.000|
|upshot_crosses_edge_def|✅ proved - incomplete|SHOSTAK|0.019|
|compute_intercept_TCC1|✅ proved - complete|SHOSTAK|0.000|
|compute_intercept_def_TCC1|✅ proved - complete|SHOSTAK|0.000|
|compute_intercept_def|✅ proved - complete|SHOSTAK|0.003|
|min_cross_dist_index_upto_TCC1|✅ proved - complete|SHOSTAK|0.000|
|min_cross_dist_index_upto_TCC2|✅ proved - complete|SHOSTAK|0.000|
|min_cross_dist_index_upto_TCC3|✅ proved - complete|SHOSTAK|0.000|
|min_cross_dist_index_upto_TCC4|✅ proved - complete|SHOSTAK|0.000|
|min_cross_dist_index_upto_TCC5|✅ proved - complete|SHOSTAK|0.000|
|min_cross_dist_index_upto_TCC6|✅ proved - complete|SHOSTAK|0.000|
|min_cross_dist_index_upto_TCC7|✅ proved - complete|SHOSTAK|0.000|
|min_cross_dist_index_upto_TCC8|✅ proved - complete|SHOSTAK|0.000|
|min_cross_dist_index_upto_TCC9|✅ proved - complete|SHOSTAK|0.000|
|min_cross_dist_index_upto_TCC10|✅ proved - incomplete|SHOSTAK|0.001|
|min_cross_dist_index_upto_TCC11|✅ proved - incomplete|SHOSTAK|0.000|
|acceptable_polygon_2D_TCC1|✅ proved - complete|SHOSTAK|0.000|
|acceptable_polygon_2D_TCC2|✅ proved - complete|SHOSTAK|0.000|
|acceptable_polygon_2D_TCC3|✅ proved - complete|SHOSTAK|0.000|
|acceptable_polygon_2D_TCC4|✅ proved - complete|SHOSTAK|0.000|
|acceptable_polygon_2D_TCC5|✅ proved - complete|SHOSTAK|0.000|
|acceptable_polygon_2D_TCC6|✅ proved - complete|SHOSTAK|0.000|
|polygon_indices_distinct|✅ proved - complete|SHOSTAK|0.001|
|acceptable_polygon_2D_def_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|acceptable_polygon_2D_def_TCC2|✅ proved - incomplete|SHOSTAK|0.000|
|acceptable_polygon_2D_def|✅ proved - incomplete|SHOSTAK|0.000|
|counterclockwise_corner_index_TCC1|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_corner_index_TCC2|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_corner_index_TCC3|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_corner_index_TCC4|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_corner_index_TCC5|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_corner_index_TCC6|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_corner_index_TCC7|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_corner_index_TCC8|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_corner_index_TCC9|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_corner_index_TCC10|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_corner_index_TCC11|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_corner_index_TCC12|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_corner_index_def|✅ proved - complete|SHOSTAK|0.000|
|min_y_val_TCC1|✅ proved - complete|SHOSTAK|0.000|
|min_y_val_TCC2|✅ proved - complete|SHOSTAK|0.000|
|min_y_val_TCC3|✅ proved - complete|SHOSTAK|0.000|
|min_y_val_TCC4|✅ proved - complete|SHOSTAK|0.000|
|min_y_val_TCC5|✅ proved - complete|SHOSTAK|0.000|
|min_y_val_TCC6|✅ proved - complete|SHOSTAK|0.000|
|min_y_val_TCC7|✅ proved - complete|SHOSTAK|0.000|
|min_y_val_TCC8|✅ proved - complete|SHOSTAK|0.000|
|min_y_val_TCC9|✅ proved - complete|SHOSTAK|0.000|
|test_point_below_TCC1|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_edges_TCC1|✅ proved - complete|SHOSTAK|0.001|
|counterclockwise_edges_TCC2|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_edges_TCC3|✅ proved - complete|SHOSTAK|0.001|
|counterclockwise_edges_TCC4|✅ proved - complete|SHOSTAK|0.000|

## `good_polygon_def`

| Formula | Proof Status | Decision Procedure | Time |
| ---     | ---          | ---                | ---  |
|straight_line_TCC1|✅ proved - complete|SHOSTAK|0.000|
|straight_line_TCC2|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_polygon?_TCC1|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_polygon?_TCC2|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_polygon?_TCC3|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_polygon?_TCC4|✅ proved - complete|SHOSTAK|0.000|

## `in_out_def`

| Formula | Proof Status | Decision Procedure | Time |
| ---     | ---          | ---                | ---  |
|arg_ac1_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|signed_angle_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|signed_angle_consec_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|signed_angle_consec_TCC2|✅ proved - incomplete|SHOSTAK|0.000|
|signed_angle_consec_TCC3|✅ proved - incomplete|SHOSTAK|0.000|
|winding_number_def_TCC1|✅ proved - complete|SHOSTAK|0.000|
|winding_number_def_TCC2|✅ proved - complete|SHOSTAK|0.000|
|winding_number_def_TCC3|✅ proved - complete|SHOSTAK|0.000|

## `angle_sum`

| Formula | Proof Status | Decision Procedure | Time |
| ---     | ---          | ---                | ---  |
|norm_angle|✅ proved - incomplete|SHOSTAK|0.001|
|norm_angle_eq|✅ proved - incomplete|SHOSTAK|0.000|
|ac_co_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|ac_co_TCC2|✅ proved - incomplete|SHOSTAK|0.000|
|signed_acos|✅ proved - incomplete|SHOSTAK|0.002|
|signed_acos2|✅ proved - incomplete|SHOSTAK|0.002|
|signed_acos3|✅ proved - incomplete|SHOSTAK|0.005|
|vect_ang_sum4|✅ proved - incomplete|SHOSTAK|0.007|
|vect_ang_sum5_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|vect_ang_sum5|✅ proved - incomplete|SHOSTAK|0.002|
|arg_ac_TCC1|✅ proved - incomplete|SHOSTAK|0.000|

## `winding_equiv`

| Formula | Proof Status | Decision Procedure | Time |
| ---     | ---          | ---                | ---  |
|wind_ang_plus_int|✅ proved - incomplete|SHOSTAK|0.000|
|quadrant_vector|✅ proved - incomplete|SHOSTAK|0.003|
|pi_bad_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|pi_bad_TCC2|✅ proved - incomplete|SHOSTAK|0.000|
|pi_bad|✅ proved - incomplete|SHOSTAK|0.002|
|contrib0|✅ proved - incomplete|SHOSTAK|0.006|
|winding_int_TCC1|✅ proved - complete|SHOSTAK|0.000|
|winding_int_TCC2|✅ proved - complete|SHOSTAK|0.000|
|winding_int_TCC3|✅ proved - complete|SHOSTAK|0.000|
|winding_int_TCC4|✅ proved - complete|SHOSTAK|0.000|
|winding_int|✅ proved - incomplete|SHOSTAK|0.003|
|base_ang_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|base_ang_TCC2|✅ proved - incomplete|SHOSTAK|0.000|
|base_ang_TCC3|✅ proved - incomplete|SHOSTAK|0.000|
|base_ang_TCC4|✅ proved - incomplete|SHOSTAK|0.000|
|base_ang_TCC5|✅ proved - incomplete|SHOSTAK|0.000|
|base_ang|✅ proved - incomplete|SHOSTAK|0.004|
|iter_winding_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|iter_winding_TCC2|✅ proved - incomplete|SHOSTAK|0.000|
|iter_winding|✅ proved - incomplete|SHOSTAK|0.102|
|origin_reduction_TCC1|✅ proved - complete|SHOSTAK|0.000|
|origin_reduction|✅ proved - incomplete|SHOSTAK|0.000|
|shifted_wnit|✅ proved - incomplete|SHOSTAK|0.000|
|shifted_wn|✅ proved - incomplete|SHOSTAK|0.000|
|shifted_defit_TCC1|✅ proved - complete|SHOSTAK|0.000|
|shifted_defit_TCC2|✅ proved - complete|SHOSTAK|0.000|
|shifted_defit_TCC3|✅ proved - incomplete|SHOSTAK|0.000|
|shifted_defit|✅ proved - incomplete|SHOSTAK|0.004|
|shifted_def_TCC1|✅ proved - complete|SHOSTAK|0.000|
|shifted_def_TCC2|✅ proved - incomplete|SHOSTAK|0.000|
|shifted_def|✅ proved - incomplete|SHOSTAK|0.000|
|definitely_inside_verification|✅ proved - incomplete|SHOSTAK|0.001|
|definitely_inside_verification2|✅ proved - incomplete|SHOSTAK|0.001|
|definitely_inside|✅ proved - incomplete|SHOSTAK|0.000|
|definitely_outside|✅ proved - incomplete|SHOSTAK|0.000|

## `polygon_contain`

| Formula | Proof Status | Decision Procedure | Time |
| ---     | ---          | ---                | ---  |
|on_any_edge?_TCC1|✅ proved - complete|SHOSTAK|0.000|
|near_any_edge_upto_TCC1|✅ proved - complete|SHOSTAK|0.000|
|near_any_edge_upto_TCC2|✅ proved - complete|SHOSTAK|0.000|
|near_any_edge_upto_TCC3|✅ proved - incomplete|SHOSTAK|0.000|
|near_any_edge_upto_TCC4|✅ proved - incomplete|SHOSTAK|0.000|
|near_any_edge_upto_TCC5|✅ proved - incomplete|SHOSTAK|0.000|
|near_any_edge_upto_TCC6|✅ proved - incomplete|SHOSTAK|0.000|
|near_any_edge_upto_def_TCC1|✅ proved - complete|SHOSTAK|0.000|
|near_any_edge_upto_def|✅ proved - incomplete|SHOSTAK|0.000|
|number_upshot_crosses_upto_TCC1|✅ proved - complete|SHOSTAK|0.000|
|number_upshot_crosses_upto_TCC2|✅ proved - complete|SHOSTAK|0.000|
|number_upshot_crosses_upto_TCC3|✅ proved - complete|SHOSTAK|0.001|
|number_upshot_crosses_upto_TCC4|✅ proved - complete|SHOSTAK|0.001|
|winding_number_rec_TCC1|✅ proved - complete|SHOSTAK|0.000|
|winding_number_rec_TCC2|✅ proved - complete|SHOSTAK|0.000|
|winding_number_rec_TCC3|✅ proved - complete|SHOSTAK|0.000|
|winding_number_rec_TCC4|✅ proved - complete|SHOSTAK|0.000|
|winding_number_rec4_TCC1|✅ proved - complete|SHOSTAK|0.000|
|winding_number_rec4|✅ proved - complete|SHOSTAK|0.012|
|winding_number_TCC1|✅ proved - complete|SHOSTAK|0.000|
|definitely_inside_prelim_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|definitely_outside_prelim_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|definitely_exclusive|✅ proved - incomplete|SHOSTAK|0.000|

## `detection`

| Formula | Proof Status | Decision Procedure | Time |
| ---     | ---          | ---                | ---  |
|on_segment_2D_sym|✅ proved - complete|SHOSTAK|0.000|
|on_segment_2D_alg_def|✅ proved - incomplete|SHOSTAK|0.002|
|dot_nneg_linear_2D_alg_TCC1|✅ proved - complete|SHOSTAK|0.000|
|dot_nneg_linear_2D_alg_TCC2|✅ proved - complete|SHOSTAK|0.000|
|dot_nneg_linear_2D_alt_typ|✅ proved - incomplete|SHOSTAK|0.002|
|dot_nneg_linear_2D_alg_def|✅ proved - incomplete|SHOSTAK|0.005|
|dot_nneg_linear_2D_alg_eq_0|✅ proved - incomplete|SHOSTAK|0.003|
|dot_nneg_spec_def|✅ proved - incomplete|SHOSTAK|0.004|
|edge_detect_simp2_def|✅ proved - incomplete|SHOSTAK|0.007|
|edge_detect_simple_def|✅ proved - incomplete|SHOSTAK|0.043|
|edge_detect_def|✅ proved - incomplete|SHOSTAK|0.001|
|Collision_Detector_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|Static_Collision_Detector_TCC1|✅ proved - incomplete|SHOSTAK|0.001|

## `convex_polygon_containment`

| Formula | Proof Status | Decision Procedure | Time |
| ---     | ---          | ---                | ---  |
|on_left_of_edge_TCC1|✅ proved - complete|SHOSTAK|0.000|
|on_left_of_edge_TCC2|✅ proved - complete|SHOSTAK|0.000|
|on_left_of_edge_TCC3|✅ proved - complete|SHOSTAK|0.000|
|all_on_left_rec_TCC1|✅ proved - complete|SHOSTAK|0.000|
|all_on_left_rec_TCC2|✅ proved - complete|SHOSTAK|0.000|
|all_on_left_rec_TCC3|✅ proved - complete|SHOSTAK|0.000|
|all_on_left_rec_TCC4|✅ proved - complete|SHOSTAK|0.000|
|all_on_left_rec_TCC5|✅ proved - complete|SHOSTAK|0.000|
|all_on_left_rec_TCC6|✅ proved - complete|SHOSTAK|0.000|
|all_on_left_rec_TCC7|✅ proved - complete|SHOSTAK|0.000|
|all_on_left_rec_TCC8|✅ proved - complete|SHOSTAK|0.000|
|all_on_left_rec_TCC9|✅ proved - complete|SHOSTAK|0.000|
|all_on_left_rec_TCC10|✅ proved - complete|SHOSTAK|0.000|
|all_on_left_rec_TCC11|✅ proved - complete|SHOSTAK|0.000|
|all_on_left_rec_TCC12|✅ proved - complete|SHOSTAK|0.000|
|all_on_left_rec_TCC13|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_convex_rec_TCC1|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_convex_rec_TCC2|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_convex_rec_TCC3|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_convex_rec_TCC4|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_convex_rec_TCC5|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_convex_def|✅ proved - complete|SHOSTAK|0.000|
|left_of_segment_2D_TCC1|✅ proved - complete|SHOSTAK|0.000|
|inside_convex_2D_rec_TCC1|✅ proved - complete|SHOSTAK|0.000|
|inside_convex_2D_rec_TCC2|✅ proved - complete|SHOSTAK|0.000|
|inside_convex_2D_rec_TCC3|✅ proved - complete|SHOSTAK|0.000|
|inside_convex_2D_rec_TCC4|✅ proved - complete|SHOSTAK|0.000|
|inside_convex_2D_rec_TCC5|✅ proved - complete|SHOSTAK|0.000|
|inside_convex_2D_rec_TCC6|✅ proved - complete|SHOSTAK|0.000|
|inside_convex_2D_rec_TCC7|✅ proved - complete|SHOSTAK|0.000|
|inside_convex_2D_rec_TCC8|✅ proved - complete|SHOSTAK|0.000|
|inside_convex_2D_rec_TCC9|✅ proved - complete|SHOSTAK|0.000|
|inside_convex_2D_TCC1|✅ proved - complete|SHOSTAK|0.000|
|inside_convex_2D_TCC2|✅ proved - complete|SHOSTAK|0.000|
|all_on_left_is_convex|✅ proved - complete|SHOSTAK|0.000|
|counterclockwise_convex_3D_is_convex|✅ proved - incomplete|SHOSTAK|0.000|

## `convex_polygon_test`

| Formula | Proof Status | Decision Procedure | Time |
| ---     | ---          | ---                | ---  |
|conterclockwise_convex_2D_rec_test|✅ proved - complete|SHOSTAK|0.000|
|conterclockwise_convex_2D_test|✅ proved - complete|SHOSTAK|0.000|
|p3Dconvex_test|✅ proved - complete|SHOSTAK|0.000|
|p64conv_TCC1|✅ proved - complete|SHOSTAK|0.000|
|p64conv_convex|✅ proved - complete|SHOSTAK|0.001|
|convex64_max|✅ proved - incomplete|SHOSTAK|0.000|
|p643D_correct|✅ proved - incomplete|SHOSTAK|0.000|

## `polygon_containment_test`

| Formula | Proof Status | Decision Procedure | Time |
| ---     | ---          | ---                | ---  |
|definitely_inside_test1|✅ proved - incomplete|SHOSTAK|0.000|
|definitely_outside_test1|✅ proved - incomplete|SHOSTAK|0.000|
|MyPoly_inside|✅ proved - incomplete|SHOSTAK|0.001|
|MyPolyTester_TCC1|✅ proved - complete|SHOSTAK|0.000|
|MyPolyTester_TCC2|✅ proved - complete|SHOSTAK|0.000|
|MyPolyTester_TCC3|✅ proved - complete|SHOSTAK|0.000|
|MyPolyTester_TCC4|✅ proved - complete|SHOSTAK|0.000|
|MyPolyTester_TCC5|✅ proved - complete|SHOSTAK|0.000|
|MyPolyTester_TCC6|✅ proved - complete|SHOSTAK|0.000|
|MyPolyTester_tr_TCC1|✅ proved - complete|SHOSTAK|0.000|
|MyPolyTester_tr_TCC2|✅ proved - complete|SHOSTAK|0.000|
|MyPolyTester_tr_def_TCC1|✅ proved - complete|SHOSTAK|0.000|
|MyPolyTester_tr_def_TCC2|✅ proved - complete|SHOSTAK|0.000|
|MyPolyTester_tr_def|✅ proved - incomplete|SHOSTAK|0.001|
|CompleteTester_tr_def|✅ proved - incomplete|SHOSTAK|0.001|

## `resolution`

| Formula | Proof Status | Decision Procedure | Time |
| ---     | ---          | ---                | ---  |
|proj_vect_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|proj_vect_TCC2|✅ proved - incomplete|SHOSTAK|0.000|
|proj_vect_TCC3|✅ proved - incomplete|SHOSTAK|0.000|
|proj_vect_TCC4|✅ proved - incomplete|SHOSTAK|0.001|
|proj_vect_TCC5|✅ proved - incomplete|SHOSTAK|0.000|
|proj_vect_TCC6|✅ proved - incomplete|SHOSTAK|0.000|
|proj_vect_TCC7|✅ proved - incomplete|SHOSTAK|0.001|
|proj_vect_TCC8|✅ proved - incomplete|SHOSTAK|0.000|
|proj_vect_TCC9|✅ proved - incomplete|SHOSTAK|0.000|
|proj_vect_TCC10|✅ proved - incomplete|SHOSTAK|0.001|
|proj_vect_norm|✅ proved - incomplete|SHOSTAK|0.001|
|modifiable_to_size_monotonic|✅ proved - incomplete|SHOSTAK|0.001|
|expand_polygon_2D_TCC1|✅ proved - incomplete|SHOSTAK|0.001|
|expand_polygon_2D_TCC2|✅ proved - incomplete|SHOSTAK|0.000|
|expand_polygon_2D_TCC3|✅ proved - incomplete|SHOSTAK|0.001|
|expand_polygon_2D_TCC4|✅ proved - incomplete|SHOSTAK|0.000|
|expand_polygon_2D_TCC5|✅ proved - incomplete|SHOSTAK|0.000|
|expand_polygon_2D_TCC6|✅ proved - incomplete|SHOSTAK|0.000|
|contract_polygon_2D_TCC1|✅ proved - incomplete|SHOSTAK|0.001|
|closest_edge_TCC1|✅ proved - complete|SHOSTAK|0.000|
|closest_edge_TCC2|✅ proved - incomplete|SHOSTAK|0.000|
|closest_edge_TCC3|✅ proved - complete|SHOSTAK|0.000|
|closest_edge_TCC4|✅ proved - complete|SHOSTAK|0.000|
|closest_edge_def_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|closest_edge_def_TCC2|✅ proved - incomplete|SHOSTAK|0.001|
|closest_edge_def|✅ proved - incomplete|SHOSTAK|0.005|
|nice_polygon_points_distinct|✅ proved - incomplete|SHOSTAK|0.000|
|recovery_test_point_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|recovery_test_point_TCC2|✅ proved - incomplete|SHOSTAK|0.001|
|recovery_test_point_TCC3|✅ proved - incomplete|SHOSTAK|0.000|
|recovery_point_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|recovery_point_TCC2|✅ proved - incomplete|SHOSTAK|0.002|
|recovery_point_TCC3|✅ proved - incomplete|SHOSTAK|0.004|
|recovery_point_TCC4|✅ proved - incomplete|SHOSTAK|0.000|
|recovery_point_TCC5|✅ proved - incomplete|SHOSTAK|0.001|
|recovery_point_TCC6|✅ proved - incomplete|SHOSTAK|0.000|
|outside_recovery_point_def|✅ proved - incomplete|SHOSTAK|0.017|
|inside_recovery_point_def|✅ proved - incomplete|SHOSTAK|0.017|

## `recurse`

| Formula | Proof Status | Decision Procedure | Time |
| ---     | ---          | ---                | ---  |
|recurse_TCC1|✅ proved - complete|SHOSTAK|0.000|
|recurse_def|✅ proved - complete|SHOSTAK|0.000|

## `time_inout`

| Formula | Proof Status | Decision Procedure | Time |
| ---     | ---          | ---                | ---  |
|quad_id_0|✅ proved - incomplete|SHOSTAK|0.000|
|quad_ivt|✅ proved - incomplete|SHOSTAK|0.001|
|dot_quad_conn|✅ proved - incomplete|SHOSTAK|0.003|
|on_segment_2D_sym|✅ proved - complete|SHOSTAK|0.000|
|on_segment_2D_alg_def|✅ proved - incomplete|SHOSTAK|0.002|
|on_segment_2D_alg_alt_def|✅ proved - incomplete|SHOSTAK|0.000|
|singular_def|✅ proved - incomplete|SHOSTAK|0.001|
|singular_def2|✅ proved - incomplete|SHOSTAK|0.001|
|dot_zero_linear_2D_alg_def|✅ proved - incomplete|SHOSTAK|0.002|
|swap_times_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|swap_times_ivt_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|swap_times_ivt|✅ proved - incomplete|SHOSTAK|0.007|
|on_segment_2D_connected|✅ proved - incomplete|SHOSTAK|0.004|
|edge_time_def_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|edge_time_def_TCC2|✅ proved - incomplete|SHOSTAK|0.000|
|edge_time_def_TCC3|✅ proved - incomplete|SHOSTAK|0.000|
|edge_time_def_TCC4|✅ proved - incomplete|SHOSTAK|0.000|
|edge_time_def_TCC5|✅ proved - incomplete|SHOSTAK|0.000|
|edge_time_def_TCC6|✅ proved - incomplete|SHOSTAK|0.000|
|edge_time_def_TCC7|✅ proved - incomplete|SHOSTAK|0.000|
|edge_time_def_TCC8|✅ proved - incomplete|SHOSTAK|0.000|
|edge_time_def_TCC9|✅ proved - incomplete|SHOSTAK|0.000|
|edge_time_def_TCC10|✅ proved - incomplete|SHOSTAK|0.000|
|edge_time_def_TCC11|✅ proved - incomplete|SHOSTAK|0.000|
|edge_time_def_TCC12|✅ proved - incomplete|SHOSTAK|0.000|
|edge_time_def|✅ proved - incomplete|SHOSTAK|0.018|

## `multipoly`

| Formula | Proof Status | Decision Procedure | Time |
| ---     | ---          | ---                | ---  |
|polygons_overlap_TCC1|✅ proved - incomplete|SHOSTAK|0.000|
|polygons_overlap_TCC2|✅ proved - incomplete|SHOSTAK|0.000|
|polygons_overlap_def|✅ proved - incomplete|SHOSTAK|0.000|
|parallel_segments_overlap|✅ proved - incomplete|SHOSTAK|0.002|
|open_segment_2Ds_cross_rew2|✅ proved - incomplete|SHOSTAK|0.009|
|on_open_segment_2Ds_cross_open|✅ proved - incomplete|SHOSTAK|0.002|
|segments_2Ds_notcross_open|✅ proved - incomplete|SHOSTAK|0.038|
|on_segment_2Ds_cross|✅ proved - incomplete|SHOSTAK|0.001|
|Moving_Polygon_Collision_Detector_def|✅ proved - incomplete|SHOSTAK|0.002|
|Static_Shape_Polygon_Collision_Detector_def|✅ proved - incomplete|SHOSTAK|0.003|

## Platform information 
|  |  |
|---|---|
| Machine Info | **LALAL2024100866** (ARM64 - Apple M3 Pro - Darwin 24.6.0) |
| PVS | 8.0 (master 2895eeec Small fixes for prover-ex.py example) |
| Lisp| SBCL 2.4.0|
| Patch Version| n/a|
| Library Path| `PolyCARP/ (master 7ec8285 Update proofs in PolyCARP_analysis to PVS 8.0)`<br/>`NASALib/ (master 7eccf4f1 PVSioParser: Improved pvsio_regex)`<br/>`$PVS_DIR/lib/ (master 2895eeec Small fixes for prover-ex.py example)`<br/>`NASALib/matrices/ (master 7eccf4f1 PVSioParser: Improved pvsio_regex)`<br/>`NASALib/float/ (master 7eccf4f1 PVSioParser: Improved pvsio_regex)`<br/>`NASALib/pvsio_utils/ (master 7eccf4f1 PVSioParser: Improved pvsio_regex)`<br/>`NASALib/dL/ (master 7eccf4f1 PVSioParser: Improved pvsio_regex)`<br/>`NASALib/algebra/ (master 7eccf4f1 PVSioParser: Improved pvsio_regex)`<br/>`NASALib/ints/ (master 7eccf4f1 PVSioParser: Improved pvsio_regex)`|
| Loaded Patches | `$HOME/.pvs.lisp`<br/>`NASALib/.pvs.lisp`|
