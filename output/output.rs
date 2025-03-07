use std::*;
use std::collections::HashMap;

const params_lances: _ = [("has_header", false), ("separator", "	"), ("na_rows", 100), ("ignore_errors", true)].iter().cloned().collect::<HashMap<_,_>>();
const df_header: _ = pl.read_csv("dados/tbl_lances_header.csv", true);
const df_lances: _ = pl.read_csv("dados/tbl_lances.csv", params_lances);
df_header;
df_lances;
const df_sample: _ = df_lances[41..44];
df;
