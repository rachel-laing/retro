# retro
A retrospective analysis of the COVID-19 pandemic and the modeling tools used throughout.

---
## Input Data
Most raw data used in this investigation is in the data/raw/ directory. This data has been culled and processed and formatted data tables used in this analysis are in the data/processed/ directory. Historical PyR0 and BVAS data exist in a different github repository, [sars-cov2-modeling](https://github.com/bkotzen/sars-cov2-modeling). Most of the raw data is publicly available at these sources:
* PyR0 historical results: [sars-cov2-modeling github](https://github.com/bkotzen/sars-cov2-modeling)
* BVAS historical results: [sars-cov2-modeling github](https://github.com/bkotzen/sars-cov2-modeling)
* Bloom fitness per mutation: [SARS2-mut-fitness github](https://github.com/jbloomlab/SARS2-mut-fitness/blob/main/results/aa_fitness/aamut_fitness_all.csv)
* Bloom DMS per mutation from [DMS Paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7418704/): [github](https://github.com/jbloomlab/SARS-CoV-2-RBD_DMS/blob/master/results/single_mut_effects/single_mut_effects.csv)
* EVEscape mutation effects (with some DMS): [EVEscape paper](https://www.nature.com/articles/s41586-023-06617-0) [Supplementary Table 6](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-023-06617-0/MediaObjects/41586_2023_6617_MOESM8_ESM.zip)
* EVEscape strain effects: `--Private repository at HMS--`
    * `/n/groups/marks/projects/CEPI/data/________/2023-10-28/all_seqs_EVEscape_scores.csv`
