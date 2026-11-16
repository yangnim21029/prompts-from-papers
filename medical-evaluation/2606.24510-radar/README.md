# 罕見疾病研究：合成與修訂訓練病例

三份公開模板用於建立訓練資料：依表型合成病例、按已知診斷修訂病例，以及補充推理。論文中的醫師輔助效果來自專門訓練的 RaDaR-32B，沒有單獨測試這些資料模板的診斷成效。

論文為 *A specialized reasoning large language model for accelerating rare disease diagnosis: a randomized AI physician assistance trial*。

作者：Haichao Chen、Songchi Zhou、Zhengyun Zhao、Shikai Hu、Xianghong Jin、Hongwei Ji、Li He、Shuli Li、Yiming Qin、Xin Tan、Runfeng Shi、Yih Chung Tham、Jiaye Zhu、Ye Li、Ye Jin、Longhao Cao、Dawei Li、Honghan Wu、Hongqiu Gu、Guanqiao Li、Tudor Groza、Chunying Li、Dian Zeng、Weihong Yu、Gareth Baynam、Saumya Shekhar Jamuar、Min Shen、Shuyang Zhang、Bin Sheng、Sheng Yu、Tien Yin Wong。

研究機構：清華大學、北京協和醫學院、新加坡國立大學、北京大學、上海交通大學等。首次提交：2026-06-23；本頁依據 arXiv:2606.24510v1。

## 研究怎麼做，結果如何

以真實與合成病例訓練RaDaR-32B推理模型，供醫師作病例診斷輔助。28家醫院84名醫師隨機分組；76名完成（AI組36、對照40）；每人五個專科病例。比較對象：可使用網路搜尋的醫師對照組。

RaDaR輔助組診斷正確率49.44%，對照28.00%，增加21.44個百分點（95%CI 11.20–31.68）；診斷時間無顯著差異。

成效依賴專門訓練模型，公開prompts主要用於資料合成；研究為病例任務而非改善患者結局的試驗；錯答時高信心更常見，不能將正確率提升等同全面更安全 錯誤診斷中，高或非常高信心占比為 RaDaR 組 65.9%、對照 27.1%；時間差為 0.14 分鐘（95% CI −1.14 至 1.41），未顯示更快。

## 公開材料與使用方式

本頁保存三份官方訓練資料模板，依程式庫 Apache 2.0 授權。論文採 arXiv non-exclusive distribution license，PDF 僅提供來源。

## 原始 prompt 與配套材料

### 1. Phenotype-to-case synthesis

給定核心及其他表型與發病年齡，合成不直接透露診斷的病例敘述。

需要提供：age_of_onset；key_phenotypes；left_phenotypes。

用途：訓練資料合成／修訂。原文範圍：官方文字檔全文，無刪節。

```text
You are an experienced clinician tasked with creating a case report for a disease. Please follow these steps: 
1. Begin by narrating the history of the present illness. Start with the key phenotypes, detailing them with the following aspects: when the symptoms first start, their duration, frequency, intensity, and any triggers that alleviate or exacerbate them. 
2. Add remaining phenotypes as accompanying phenotypes. Also, add some accompanying positive or negative symptoms not listed in the phenotype list. 
3. Expand on whether the patient has previously sought medical attention or received any treatment elsewhere, the outcomes of these examinations, and how the patient responded to treatment. Incorporate any notable incidents or changes that occurred during the progression of the disease. 
4. Next, focus on the physical examination considering all phenotypes (both key and non-key). Describe both positive and negative physical examination findings. 
5. Proceed to comprehensively describe the results of the patient's auxiliary tests, ensuring coverage of all phenotypes. Include at least 2-3 auxiliary test results for a phenotype. Specify reference ranges for test values and use decimal precision where relevant. 
6. Add some regular negative test results.

The case summary should begin with: "A (age of onset) male/female " and be narrated in an unstructured text format without section headings. 
Please be completely objective and do not summarize, conclude, suggest and interpret. Don't mention the diagnosis. Instead, rephrase phenotypes appropriately to maintain objectivity and professionalism.

Here is the information you need for synthesis. 
The key phenotypes include {key_phenotypes}.
The non-key phenotypes include {left_phenotypes}.
The age on onset is {age_of_onset}.
```

原檔：`upstream/sample/prompt_case_syn.txt`。來源定位：`sample/prompt_case_syn.txt`。

### 2. Diagnosis-conditioned case revision

用已知診斷檢查合成病例的矛盾，保留合理細節，補上必要臨床特徵。

需要提供：case；diagnosis。

用途：訓練資料合成／修訂。原文範圍：官方文字檔全文，無刪節。

```text
You are a rare disease expert tasked with evaluating the reasonability of a clinical case. Follow these steps: 
1. Remove/modify the contradictory parts (e.g., phenotypes, descriptions, duration, age of onset, chronicity, or other details) based on the final diagnosis. 
2. Retain all plausible details, even if they are irrelevant to or don't support the diagnosis, as long as they do not contradict the diagnosis. 
3. Add clinical details that are necessary or highly indicative to the diagnosis. 
The final case should be fully objective in free texts without any interpretations. Don't directly mention the diagnosis in the case (it's OK in “reasoning”). Don't simplify the case in any way. 
Respond in JSON format with one key 'Reasoning' and the other key 'Modified Case'. The output should be like this: 
"Reasoning": reasoning following the upper three steps, "Modified Case": case in free text.
Here is the diagnosis: {diagnosis}
Here is the case: {case}
```

原檔：`upstream/sample/prompt_case_modify.txt`。來源定位：`sample/prompt_case_modify.txt`。

### 3. Reasoning-data revision

對既有病例的推理訓練文本及答案插入指定診斷的分析；屬研究資料製作模板。

需要提供：COT；case；diagnosis；final_answer。

用途：訓練資料合成／修訂。原文範圍：官方文字檔全文，無刪節。

```text
You will be provided a case, and its corresponding chain of thoughts and final diagnosis answer. Please help by modifying the COT and the final diagnosis answer by inserting an analysis of the diagnosis “{diagnosis}” where you think is most appropriate.
 
Try to keep the original COT unchanged, except for the insertion. Output the entire COT without omission, including even the parts that remain unchanged—just repeat them as they are.
 
Don't emphasize or highlight the diagnosis. 
 
Format your answer in the following JSON structure: 
“modified_COT”: modified COT; 
“modified_answer”: modified answer;
 
Here is the case: {case}
Here is the COT: {COT}
Here is the final answer: {final_answer}
```

原檔：`upstream/sample/cot_modify.txt`。來源定位：`sample/cot_modify.txt`。

## 來源與授權

論文授權：arXiv non-exclusive distribution license。模板、程式與資料各自沿用來源授權；逐檔授權、處理方式、固定版本與 SHA-256 列於來源清單。

[arXiv 論文](https://arxiv.org/abs/2606.24510v1) · [官方程式固定版本](https://github.com/sczzz3/RaDaR/tree/f3334c76e90340e4c78062401edf71ccfaee3f68) · [逐檔來源與授權](../../sources.json)

來源查核與整理日期：2026-11-16。中文導讀為本庫整理；原始模板保留來源文字。
