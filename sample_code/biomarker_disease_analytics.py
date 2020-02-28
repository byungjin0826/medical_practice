import pandas as pd
from pandas import crosstab
import matplotlib.pyplot as plt
import seaborn as sns
from google.cloud import bigquery


project_id = 'biomarker'
client = bigquery.Client(project=project_id)


# OCIDs(OntoChem's Ontology Concept IDs)
# Nervous System Diseases, OCID: 208000009025

disease_ocid = 208000009025


query = """
SELECT  mkr.termFields.biomarker AS marker, 
        mkr.conceptFields.biomarker AS marker_ocid, 
        mkr_pl_tbl.name AS marker_lbl,
        mkr.termFields.biomarker_target AS target, 
        mkr.conceptFields.biomarker_target AS target_ocid,
        tgt_pl_tbl.name AS target_lbl,
        termFields.source_id AS src_id,
        termFields.srcrep AS src_repo
FROM `biomarker.relationships.dbrel` mkr
INNER JOIN ( 
    SELECT DISTINCT ocid 
    FROM `biomarker.ontologies.diseases_ancestors` 
    WHERE parent_ocid = {ocid}
) nsd ON nsd.ocid = mkr.conceptFields.biomarker_target
LEFT JOIN `biomarker.ontologies.full_preflabel` mkr_pl_tbl ON mkr_pl_tbl.ocid = mkr.conceptFields.biomarker
LEFT JOIN `biomarker.ontologies.full_preflabel` tgt_pl_tbl ON tgt_pl_tbl.ocid = mkr.conceptFields.biomarker_target
WHERE mkr.conceptFields.biomarker_target IS NOT NULL
AND mkr.conceptFields.biomarker IS NOT NULL
""".format(ocid=disease_ocid)

query_job = client.query(query, location="US")
df = query_job.to_dataframe()
