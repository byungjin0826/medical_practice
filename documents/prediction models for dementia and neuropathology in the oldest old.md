# prediction models for dementia and neuropathology in the oldest old

## Abstract
- Background:
    - 

- Methods:
    - data
        - 최소한 2년간 추적한 245명
        - autopsy data 163명(for pathology)
    - sociodemographic(사회인구통계?), cognitive(인지), clinical, vascular(혈관), lifestyle, APOE genotype
    - Neuropathological assessmets는 beta-amyloid, neurofibrillary tagles(신경섬유?), neuritic plaques(신경 전염병), etc를 포함
    
- Results
    - validation: 10 X 10-fold cross-validation
    - AUC
        - dementia: 0.73
        - Alzheimer's disease or amyloid related: 0.64 - 0.68
        - macroinfarcts: 0.72
        - microinfarcts: 0.61
        
        
## Background

## Methods
### Study population
- 1991년에 85세 이상을 대상으로 601명 중 11명 거절, 1명 연락불가, 1명 사망 등의 사유로 588명
- 35명이 더 사망, 553명
- 실험 시작일에 214명은 dementia에 걸렸고, 339명은 괜찮았음

- 1994년, 96년 99년 , 2001년에 재검사

- 사망까지 101명이 추가적으로 dementia 판정 받음

- 사후 검사가 실시되어 

- 사망의 영향을 줄이기 위해 시험시작일에 치매가 없던 339명 중 2년 내에 사망한 93명의 참가자는 모델에서 제외

- 245명을 최종적으로 예측 모델.

### Assessment of factors included in prediction models
- baseline clinical evaluation
    - examination by physician
    - interview on their health, behavior, medication by nurse
- medical history
- sociodemographic factors
    - age
    - sex
    - years of formal education
    - social class
- cognition
    - Mini Mental State Examination(MMSE)
    - Short Portable Mental Status Questionnarie(SPMSQ)
- subjective memory decline
- functional ability
    - activities of daily living
    - instrumental activities of daily living
- self-rating depression scale
- comorbidities(동반질환)
    - diabetes
    - cardiovascular condition
        - angina pectoris
        - heart infarction
        - atrial fibrillation
        - heart failure
        - arteriosclerosis obliterans
        - hypertension
    - cerebrovascular conditions
        - stroke 
        - transient
- vascular and lifestyle-related factor
    - systolic and diastolic blood pressure
    - BMI
    - alcohol use
    - smoking
- cholesterol
    - HDL
    - LDL
    - APOE genotyping
    - PCR

### dementia diagnosis
- dementia
    - Diagnostic and Statistical Manual of Mental Disoders
- AD and vascular dementia
    - National Institute of Neurological and Communicative Disorders
    - National Institute of Neurological Disorders and Stroke Association Internationale

### neuropathological assessment
- 

### Disease State Index
- supervised learning method
    - for predicting disease outcomes
    - differential diagnostics as a clinical decision-making tool
- larger amounts of heterogeneous data
- handle missing data
- use unprocessed data without prespecified cutoffs
    - combining all cognitive tests
- useful for filtering noise
- preventing strongly correlated factors

- other methods
    - logistic regression
    - svm
    - Bayes inference
    - 
    
- 0에 가까우면
    - 건강
- 1에 가까우면
    - dementia or pathology

- 각 요인들의 fitness function을 계산
    - share of false-negative errors / sum of false-negative and false-positive errors
    