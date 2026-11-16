# Prompts from Papers

收錄 2026 年 34 篇研究與作者公開的 prompt，依八類用途整理。每篇說明研究如何比較、實際得到什麼結果、公開模板需要哪些輸入，以及哪些部分尚未公開。可保存的原始模板直接列在說明頁，並附獨立檔案；較長的科研與評分材料按工作階段分頁。

這次收錄以原先的 34 篇文獻清單為範圍，並非今年 arXiv 的完整普查。大學與研究機構依論文標示，包含劍橋、史丹佛、MIT、賓大、哥倫比亞等團隊，也保留企業研究。

## 怎麼使用

先依下方用途開啟一篇說明頁，閱讀「公開材料與使用方式」，再選需要的模板。頁面會列出要填的變數、工具、範例或資料。多代理、檢索和模型訓練的研究，另說明整套流程與單份 prompt 的關係。

本庫收錄任務指令，也收錄評分、模擬與資料處理模板，逐份標明用途。研究的正面結果不一定來自 prompt 本身；有些測的是 AI 存取權、教學安排、多代理流程或微調模型。比較對象、未達顯著的結果與重現限制都留在各篇說明中。

## 實際產出對照

每種任務各用一份 200–300 字中文素材，讓論文 prompt 與 AI 另寫的短 prompt 各跑兩次，共保存 12 份完整回覆。產出與執行紀錄原樣呈現，供讀者自行比較。

| 任務 | 素材字數 | 對照 |
|---|---:|---|
| [清晰度修訂](examples/clarity/) | 232 | 短 prompt 與論文清晰度修訂模板 |
| [角色敘事](examples/narrative/) | 225 | 短 prompt 與角色敘事模板 |
| [詩歌細讀](examples/close-reading/) | 235 | 短 prompt 與原始細讀指示 |

實際回傳模型為 Gemini 3.6 Flash。這些是本庫的實作紀錄；原論文的實驗另見各篇說明。新增文獻目前收錄來源與模板，尚未逐篇執行產出對照。

## 寫作與閱讀（5 篇）

從構思、起草、修訂到角色敘事與文本細讀。風格模仿的 prompting 與微調結果分開說明。

| 用途與完整說明 | 研究機構 | 收錄材料 |
|---|---|---|
| [角色建構與故事生成](story-generation/2608.10337-narrative-keyframing/)<br>2608.10337 | 康乃爾大學 | 8 份原始模板與敘事產出對照 |
| [文學風格模仿](style-imitation/2601.18353-good-writing/)<br>2601.18353 | 密西根大學、石溪大學 | 50 位作家的原始來源；本庫另附改編模板 |
| [詩歌細讀與解釋](close-reading/2603.06855-poem-interpretation/)<br>2603.06855 | 芝加哥大學、杜克大學 | 原始任務指示與產出對照 |
| [人機共寫與獎勵制度](human-ai-cowriting/2604.03529-incentives/)<br>2604.03529 | 麻省理工學院 | 多輪提示紀錄與品質評分模板 |
| [寫作規劃、起草與修訂](writing-revision/2604.11009-planning-to-revision/)<br>2604.11009 | 雪梨大學、哥倫比亞大學、約翰霍普金斯大學、密西根大學 | 7 份原始模板與清晰度產出對照 |

## 教學與學習（10 篇）

涵蓋教案、逐步教學、程式回饋、個人化練習及學習評分。每篇標明結果衡量的是考試、作品品質，或對話行為。

| 用途與完整說明 | 研究機構 | 收錄材料 |
|---|---|---|
| [GRE 家教：規劃教案與逐題引導](education-learning/2609.28470-studentbench/)<br>2609.28470 | Handshake AI研究團隊（企業） | GRE 教案與家教；8 份完整教學模板，另附專家評分表 |
| [MBA 財務家教：分層追問與評分](education-learning/2609.23958-voice-tutors/)<br>2609.23958 | 波士頓大學Questrom商學院 | 財務家教與 SOLO 評分；導師 prompt 為公開節錄 |
| [人格適配教學：模擬學生與選擇教學策略](education-learning/2601.08402-pats/)<br>2601.08402 | 蘇黎世聯邦理工學院（ETH Zurich）、Bocconi University、蘇黎世大學 | 學生模擬、人格適配教師與教學評估 |
| [圖文教材問答：檢索文字、圖片與對話](education-learning/2604.02221-mudoc/)<br>2604.02221 | 喬治亞理工學院、德州大學奧斯汀分校 | 3 種學習系統與 3 份教材前處理模板 |
| [程式除錯提示：先自己判斷，再用 AI 協助](education-learning/2604.19931-deferred-hints/)<br>2604.19931 | 密西根大學、德州大學奧斯汀分校、KAIST、Learning Data Insights | 除錯提示模板；原文僅提供來源連結 |
| [程式作業回饋：測試案例與自然語言提示](education-learning/2606.08807-programming-feedback/)<br>2606.08807 | 麻薩諸塞大學阿默斯特分校 | 完整測試案例回饋與自然語言除錯提示 |
| [高中家教：依對話切換教學策略](education-learning/2606.20138-adaptive-tutoring/)<br>2606.20138 | 萊頓大學（Leiden University）、FutureWhiz | 策略片段、基礎結構與評估；完整商業 prompt 未公開 |
| [好奇心教學：調整提問與探索方向](education-learning/2606.22349-curiobot/)<br>2606.22349 | 卡內基美隆大學、新加坡管理大學 | 兩階段教學、對話評分與探索行為量表 |
| [AI 學習實驗：作文評分與使用方式分類](education-learning/2607.08849-learning-impact/)<br>2607.08849 | Middlebury College；IZA（作者研究聯盟 affiliation） | 寫作測驗、作文評分與使用方式分類；非固定教學 prompt |
| [Python 個人化家教：出題、輔導與答案評分](education-learning/2608.16907-personalized-python/)<br>2608.16907 | 賓州大學、國立臺灣大學 | 出題、Python 家教與評分；部分請求組件未公開 |

## 創意發想與產品設計（2 篇）

一篇比較多代理與人類團隊的創意；另一篇研究讓團隊在何時取得 AI 協助。

| 用途與完整說明 | 研究機構 | 收錄材料 |
|---|---|---|
| [多代理創意發想：產生、討論與篩選點子](creativity-product-design/2605.17885-multi-agent-creativity/)<br>2605.17885 | University of Cambridge、Zhejiang University、Microsoft Research Asia、Universitat Politècnica de València | 任務、創意生成、討論、篩選與評分模板 |
| [產品發想：依團隊階段提供 AI 協助](creativity-product-design/2610.14984-ai-timing-product-design/)<br>2610.14984 | Chinese Academy of Sciences, Academy of Mathematics and Systems Science、Zhejiang University, School of Management | 產品設計助理、實驗任務與創意評分規準 |

## 訪談、市調與質性分析（4 篇）

訪綱追蹤、追問、需求擷取、編碼與數位分身。資料量、洞見品質與預測準確度分開呈現。

| 用途與完整說明 | 研究機構 | 收錄材料 |
|---|---|---|
| [質性分析：整理據點摘要與跨訪談證據](interviews-qualitative-analysis/2601.14478-qualitative-health-research/)<br>2601.14478 | Stanford University（史丹佛大學）、Harvard University（哈佛大學）、Impactivo LLC | 主題整理、跨據點綜整與證據檢索；原文僅提供連結 |
| [半結構式訪談：追蹤訪綱與發現新主題](interviews-qualitative-analysis/2602.21136-sparkme/)<br>2602.21136 | Stanford University（史丹佛大學） | 訪綱管理、新主題辨認、模擬受訪者與評估 |
| [市場研究：擷取需求與建立消費者分身](interviews-qualitative-analysis/2609.29143-market-research-twins/)<br>2609.29143 | Columbia University（哥倫比亞大學）、University of Pennsylvania（賓州大學） | 需求擷取、數位分身、行銷任務與評估 |
| [文字訪談：依訪綱追問、分類與改寫問題](interviews-qualitative-analysis/2610.23149-ai-led-interviews/)<br>2610.23149 | University of Copenhagen（哥本哈根大學）、IT University of Copenhagen | 追問、判斷、問題改寫與完整訪綱 |

## 個人教練與溝通（4 篇）

具體目標設定、同理溝通練習與支持回覆。目標進展研究所公開的材料主要是事後編碼模板。

| 用途與完整說明 | 研究機構 | 收錄材料 |
|---|---|---|
| [目標設定：把模糊願望寫成具體行動](coaching-communication/2602.08636-effective-goal-setting/)<br>2602.08636 | University of Cambridge、LMU Munich、Munich Center for Machine Learning (MCML)、Technical University of Munich | 具體目標回饋、函式格式、固定引導與建議 |
| [同理溝通練習：角色扮演與具體回饋](coaching-communication/2603.15245-empathic-communication/)<br>2603.15245 | Northwestern University（西北大學）、Stanford University（史丹佛大學） | 角色扮演、同理溝通教練與評分 |
| [目標進展研究：目標與回饋的事後編碼](coaching-communication/2603.17887-goal-progress-accountability/)<br>2603.17887 | University of Cambridge、Technical University of Munich | 3 份研究編碼模板僅提供連結；教練 prompt 未找到 |
| [網路騷擾情境：產生支持回覆](coaching-communication/2606.05995-empathy-on-demand/)<br>2606.05995 | University of Geneva（日內瓦大學）、University of St. Gallen（聖加侖大學） | 完整支持回覆 prompt；3 個情境欄位 |

## 科研與文獻回顧（5 篇）

研究構想、實驗程式、理論修訂、解題評論與文獻篩選。多數需要工具、資料和多輪流程配合。

| 用途與完整說明 | 研究機構 | 收錄材料 |
|---|---|---|
| [科研代理：累積研究方向與實驗經驗](scientific-research/2603.08127-evoscientist/)<br>2603.08127 | Huawei Technologies、阿姆斯特丹自由大學、萊頓大學 | 研究記憶、構想評分與科研代理模板 |
| [理論物理解題：解題者、評論者與評分者](scientific-research/2605.06772-scalar/)<br>2605.06772 | 克里特大學、倫敦瑪麗女王大學、蘇黎世大學、CERN | 多輪解題、評論、修訂與評分；評論者需參考答案 |
| [認知科學研究：提出實驗、比較理論與修訂模型](scientific-research/2606.26448-autocog/)<br>2606.26448 | 普林斯頓大學、康乃爾大學、史丹佛大學、Helmholtz Munich | 實驗設計、結果解讀、理論修訂與模型批評 |
| [科研工作流程：構想、執行、消融與任務規格](scientific-research/2610.18933-agentic-scientist/)<br>2610.18933 | Sakana AI（企業研究團隊） | 4 份論文核心模板；另附官方科研、寫作與流程模板 |
| [系統性文獻回顧：篩選準則與資料擷取](scientific-research/2610.21042-reviewpilot/)<br>2610.21042 | 亞利桑那大學、佛羅里達國際大學、Vanderbilt、UC Irvine、紐約大學、UIUC、Broad Institute of MIT and Harvard等 | 篩選、資料擷取與領域規則；原文僅提供來源連結 |

## 醫療研究與評估（2 篇）

病例訓練資料與臨床答案評分。兩篇的主要改善都涉及模型訓練，公開模板的角色另行說明。

| 用途與完整說明 | 研究機構 | 收錄材料 |
|---|---|---|
| [罕見疾病研究：合成與修訂訓練病例](medical-evaluation/2606.24510-radar/)<br>2606.24510 | 清華大學、北京協和醫學院、新加坡國立大學、北京大學、上海交通大學等 | 3 份病例訓練資料模板；研究效益涉及模型訓練 |
| [醫療 AI 評估：依臨床量表評閱答案](medical-evaluation/2609.12822-preceptron/)<br>2609.12822 | 哈佛醫學院、史丹佛大學、MIT、BIDMC、University of Alberta、Erasmus MC、University of Maryland等 | 臨床答案評分與量表；一致性提升主要來自微調 |

## 工作決策與資料分析（2 篇）

商業問題分析、任務評分，以及協作 notebook 的規則檢查與 prompt 修訂。

| 用途與完整說明 | 研究機構 | 收錄材料 |
|---|---|---|
| [商業問題分析：任務助理、評分與對話分類](work-data-analysis/2608.04198-education-productivity-gap/)<br>2608.04198 | University of Nottingham、Universidad de San Andrés、University of Maryland、NBER、Universidad Torcuato Di Tella | 4 份助理模板；另附評分、量表、圖表與使用分類 |
| [協作資料分析：送出 prompt 前檢查團隊規則](work-data-analysis/2608.04331-intentlint/)<br>2608.04331 | University of Waterloo | 規則檢查、prompt 修訂與規則建議 |

## 原文、PDF 與授權

以下四篇已核對公開模板，但未找到可供本庫重刊長文的授權，因此保留用途、輸入與原始來源連結：Hint-Writing with Deferred AI Assistance（2604.19931）、AI-Assisted Goal Setting（2603.17887）、Large-Scale Qualitative Analysis（2601.14478）、ReviewPilot（2610.21042）。其他篇也可能包含原文節錄、缺少上下文的模板，或只提供外部連結的部分；完整範圍逐項標示。

論文 PDF 僅在授權允許時保存。原始模板保留來源措辭；各檔案沿用各自授權，包含 CC BY、CC BY-NC-SA、CC BY-NC-ND、MIT、Apache、GPL 與 AGPL。作家風格填空模板標為改編，額外撰寫的[中文局部修改模板](templates/)獨立存放。

[CSV 文獻清單](catalog.csv) · [完整 JSON 文獻與模板清單](catalog.json) · [逐檔來源、版本與 SHA-256](sources.json) · [作者歸屬與授權](ATTRIBUTION.md)

本次擴充與來源查核：2026-11-16。原有五篇寫作／閱讀導讀與產出對照保留原整理紀錄；個別日期見各頁及清單。中文導讀以 AI 輔助整理並核對來源。
