# 來源與授權

每份第三方內容依自己的來源與授權使用；本 repository 沒有替整批材料套上同一份授權。

| 內容 | 作者或來源 | 授權 |
|---|---|---|
| [寫作規劃與局部修訂](writing-revision/2604.11009-planning-to-revision/) 的論文 PDF | Katy Ilonka Gero；Tao Long；Carly Schnitzler；Paramveer S. Dhillon · [arXiv](https://arxiv.org/abs/2604.11009v2) | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) |
| [範文與風格模仿](style-imitation/2601.18353-good-writing/) 的論文 PDF | Tuhin Chakrabarty；Paramveer S. Dhillon · [arXiv](https://arxiv.org/abs/2601.18353v1) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| [角色與故事生成](story-generation/2608.10337-narrative-keyframing/) 的論文 PDF | Chao Zhang；Abe Davis · [arXiv](https://arxiv.org/abs/2608.10337v1) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| [詩歌細讀與解釋](close-reading/2603.06855-poem-interpretation/) 的論文 PDF | Jiayin Zhi；Hoyt Long；Richard Jean So；Mina Lee · [arXiv](https://arxiv.org/abs/2603.06855v1) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| [人機共寫與多輪修改](human-ai-cowriting/2604.03529-incentives/) 的論文 PDF | Nathanael Jo；Manish Raghavan · [arXiv](https://arxiv.org/abs/2604.03529v2) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |

- From Planning to Revision 的 7 份模板：擷取附錄 C，僅移除 HTML 排版，依 CC BY-NC-SA 4.0 保留作者歸屬與相同授權。
- Narrative Keyframing 的模板：擷取附錄 A，僅移除 HTML 排版，依 CC BY 4.0。
- 詩歌細讀任務：擷取 [close-reading-interface](https://github.com/xxxxbrandieeee/close-reading-interface) 的 `page5_1.left_top_instruction`，僅移除 HTML，保留 [MIT 授權全文](close-reading/2603.06855-poem-interpretation/prompts/LICENSE-MIT.txt)。Copyright (c) 2026 jiayin-3zh-research。
- 人機共寫：評分模板取自附錄 B.2，使用者紀錄取自 [公開資料集](https://huggingface.co/datasets/nathanaeljo/ai-cocreation-incentives)，作者 Nathanael Jo 與 Manish Raghavan，均為 CC BY 4.0。兩份 CSV 未修改；瀏覽範例選取前 5 筆非空使用者紀錄。
- 作家風格填空模板：依論文方法另行撰寫，標記為 adapted；上游 50 份完整 prompt 只列連結，沒有轉載文學作品節錄。
- 中文補充模板及導讀為本次整理內容，未代表原論文作者的建議或額外實驗結果。

[sources.json](sources.json) 記錄逐檔來源、內容處理、擷取日期與 SHA-256。PDF 保留原始版本，沒有改動內容。

## 本庫產出示範

[examples](examples/) 中的三份中文素材為整理時撰寫的虛構文本；短 prompt 與十二份任務產出由 Gemini API 實際生成，回傳模型版本均為 Gemini 3.6 Flash。對照頁保存模型原始產出與執行資料，由讀者自行比較。

填入素材的論文 prompt 及包含該原文的請求檔，保留各自來源授權：清晰度修訂採 CC BY-NC-SA 4.0，敘事模板採 CC BY 4.0，細讀任務採 MIT。模板調整記錄於各示範頁及 case.json；模型請求、回覆與檔案雜湊見 [examples/manifest.json](examples/manifest.json)。

## 2026-11-16 擴充的 29 篇

下表列出新增研究的作者歸屬與實際保存材料。PDF 與程式授權分別核對；程式來源的授權不延伸到論文。原始檔的網址、固定 commit、處理方式與 SHA-256 均列於 sources.json。

| 論文 | 作者 | 保存材料的授權 |
|---|---|---|
| [StudentBench: AI and human tutoring yield equivalent GRE learning gains](education-learning/2609.28470-studentbench/) | Northcutt, Curtis、Hasmani, Inaara、Feng, Kevin、Khangi, Trevor、Plesner, Andreas、Mueller, Jonas | CC BY 4.0 |
| [When AI Tutors Speak: Evidence from a Randomized Field Experiment](education-learning/2609.23958-voice-tutors/) | Yang, Shihao、Van Alstyne, Marshall、Dellarocas, Chrysanthos | CC BY-NC-ND 4.0 |
| [PATS: Personality-Aware Teaching Strategies with Large Language Model Tutors](education-learning/2601.08402-pats/) | Rooein, Donya、Chowdhury, Sankalan Pal、Eremeeva, Mariia、Qin, Yuan、Nozza, Debora、Sachan, Mrinmaya、Hovy, Dirk | CC BY 4.0 |
| [Impact of Multimodal and Conversational AI on Learning Outcomes and Experience](education-learning/2604.02221-mudoc/) | Taneja, Karan、Singh, Anjali、Goel, Ashok K. | Apache-2.0；factual metadata |
| [Hint-Writing with Deferred AI Assistance: Fostering Critical Engagement in Data Science Education](education-learning/2604.19931-deferred-hints/) | Singh, Anjali、Brooks, Christopher、Li, Warren、Kim, Juho、Wang, Xu | CC BY 4.0；prompt 僅連結 |
| [A Classroom Study of LLM-Generated Feedback Intervention in Introductory Programming](education-learning/2606.08807-programming-feedback/) | Heickal, Hasnain、Lan, Andrew | CC BY 4.0 |
| [Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring](education-learning/2606.20138-adaptive-tutoring/) | Chang, Po-Chin、Hogan, Nicholas、Plaat, Aske、van der Meer, Michiel T. | CC BY 4.0 |
| [Curiosity as Linguistic Intervention: Using LLM Tutoring Dialogues to Influence Exploratory Learning Behavior](education-learning/2606.22349-curiobot/) | Ganganath, Gevindu、Bolonghege, Pasindu、Lyu, Qianru、Varakantham, Pradeep、Kandappu, Thivya | CC BY-NC-ND 4.0 |
| [Experimental Evidence on the Learning Impact of Generative AI](education-learning/2607.08849-learning-impact/) | Contractor, Zara、Reyes, Germán | CC BY 4.0 |
| [Effective Personalized AI Tutors via LLM-Guided Reinforcement Learning](education-learning/2608.16907-personalized-python/) | Chung, Angel Tsai-Hsuan、Zhang, Botong、Kung, Ling-Chieh、Bastani, Hamsa、Bastani, Osbert | CC BY 4.0 |
| [EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery](scientific-research/2603.08127-evoscientist/) | Yougang Lyu、Xi Zhang、Yuyue Zhao、Konstantinos Papakostas、Xinhao Yi、Shuyu Guo、Wenxiang Hu、Jan Piotrowski、Jakub Kaliski、Jacopo Urbani、Zaiqiao Meng、Lun Zhou、Zhaochun Ren、Xiaohui Yan | CC BY 4.0；Apache-2.0 |
| [When Does Critique Improve AI-Assisted Theoretical Physics? SCALAR: Structured Critic–Actor Loop for Agentic Reasoning](scientific-research/2605.06772-scalar/) | Vasilis Niarchos、Constantinos Papageorgakis、Alexander G. Stapleton、Sokratis Trifinopoulos | GPL-2.0 |
| [A specialized reasoning large language model for accelerating rare disease diagnosis: a randomized AI physician assistance trial](medical-evaluation/2606.24510-radar/) | Haichao Chen、Songchi Zhou、Zhengyun Zhao、Shikai Hu、Xianghong Jin、Hongwei Ji、Li He、Shuli Li、Yiming Qin、Xin Tan、Runfeng Shi、Yih Chung Tham、Jiaye Zhu、Ye Li、Ye Jin、Longhao Cao、Dawei Li、Honghan Wu、Hongqiu Gu、Guanqiao Li、Tudor Groza、Chunying Li、Dian Zeng、Weihong Yu、Gareth Baynam、Saumya Shekhar Jamuar、Min Shen、Shuyang Zhang、Bin Sheng、Sheng Yu、Tien Yin Wong | Apache-2.0 |
| [Closing the Loop to Discover Psychological Theories with an Automated Cognitive Scientist](scientific-research/2606.26448-autocog/) | Akshay K. Jagadish、Younes Strittmatter、Nori Jacoby、George Kachergis、Eric Schulz、Nathaniel Daw、Suyog H. Chandramouli、Thomas L. Griffiths | CC BY 4.0；MIT |
| [Scaling Clinical Judgment to Evaluate Medical AI](medical-evaluation/2609.12822-preceptron/) | Thomas A. Buckley、Zahir Kanjee、Peter G. Brodeur、Byron Crowe、Anthony M. Pettinato、Aashna P. Shah、Adrian D. Haimovich、Liam G. McCoy、Daniel Restrepo、Jason A. Freed、Ethan Goh、Jonathan H. Chen、Laura Zwaan、Katherine E. Goodman、Daniel J. Morgan、Raja-Elie E. Abdulnour、Adam Rodman、Arjun K. Manrai | MIT |
| [The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery](scientific-research/2610.18933-agentic-scientist/) | Robert Tjarko Lange、Luca Grillotti、Yutaro Yamada、Rujikorn Charakorn、David Ha | CC BY 4.0；Apache-2.0 |
| [ReviewPilot: A Multi-Agent System for Screening and Data Extraction in Systematic Reviews](scientific-research/2610.21042-reviewpilot/) | Zhaoqian Xue、Shaoze Zhou、Xuexin Li、Junting Mu、Haozheng Liu、Zhongyin Wang、Yichun He、Renkai Ma、Hao Zhou、Sarah Bratt、Siyuan Ma、Chen Chen、Lingyao Li | 僅提供來源連結，未重刊 PDF 或模板 |
| [Multi-agent AI systems outperform human teams in creativity](creativity-product-design/2605.17885-multi-agent-creativity/) | Tiancheng Hu、Yixuan Jiang、Haotian Li、José Hernández-Orallo、Xing Xie、Nigel Collier、David Stillwell、Luning Sun | CC BY-NC-SA 4.0 |
| [Supporting Effective Goal Setting with LLM-Based Chatbots](coaching-communication/2602.08636-effective-goal-setting/) | Michel Schimpf、Sebastian Maier、Anton Wyrowski、Lara Christoforakos、Stefan Feuerriegel、Thomas Bohné | CC BY 4.0 |
| [AI-Assisted Goal Setting Improves Goal Progress Through Social Accountability](coaching-communication/2603.17887-goal-progress-accountability/) | Michel Schimpf、Julian Voigt、Thomas Bohné | 僅提供來源連結，未重刊 PDF 或模板 |
| [Does generative AI narrow education-based productivity gaps? Evidence from a randomized experiment](work-data-analysis/2608.04198-education-productivity-gap/) | Guillermo Cruces、Diego Fernández Meijide、Sebastian Galiani、Ramiro H. Gálvez、María Lombardi | CC BY 4.0；GPL-3.0 (upstream LICENSE) |
| [IntentLint: Supporting Intent Scaffolding and Prompt-time Linting in Human-AI Collaborative Data Analysis](work-data-analysis/2608.04331-intentlint/) | Felicia Li Feng、Jian Zhao、Anamaria Crisan | CC BY 4.0 |
| [Too Late to Prune: Generative AI, the Screen, and Team Creative Decisions](creativity-product-design/2610.14984-ai-timing-product-design/) | Difang Huang、Shumin Yu、Fadong Chen、Weihua Zhou | CC BY 4.0 |
| [Large Language Models for Large-Scale, Rigorous Qualitative Analysis in Applied Health Services Research](interviews-qualitative-analysis/2601.14478-qualitative-health-research/) | Sasha Ronaghi、Emma-Louise Aveling、Maria Levis、Rachel L. Ross、Emily Alsentzer、Sara Singer, for the iPATH investigators | CC BY 4.0；prompt 僅連結 |
| [SparkMe: Adaptive Semi-Structured Interviewing for Qualitative Insight Discovery](interviews-qualitative-analysis/2602.21136-sparkme/) | David Anugraha、Vishakh Padmakumar、Diyi Yang | CC BY 4.0 |
| [Practicing with Language Models Cultivates Human Empathic Communication](coaching-communication/2603.15245-empathic-communication/) | Aakriti Kumar、Nalin Poungpeth、Diyi Yang、Bruce Lambert、Matthew Groh | CC BY 4.0 |
| [Empathy on Demand: How Empathic AI Can Scale Emotional Support for Verbal Harassment](coaching-communication/2606.05995-empathy-on-demand/) | Anouk Bergner、Philipp Winder、Christian Hildebrand | CC BY 4.0；MIT |
| [AI-Moderated Interviews for Market Research and Digital Twins Calibration](interviews-qualitative-analysis/2609.29143-market-research-twins/) | Yuting Deng、Jingxuan Liu、Olivier Toubia、Naman Jain | CC BY 4.0 |
| [Can AI interview? Comparing AI-led to Human-led Chat Interviews](interviews-qualitative-analysis/2610.23149-ai-led-interviews/) | Semra Guven、Tobias Gårdhus、Andreas Bjerre-Nielsen、Anna Rogers、Hjalmar Bang Carlsen | CC BY 4.0；AGPL-3.0 |

上游程式與 skill 文件作為研究材料保存，其操作指令不構成本專案的執行要求。論文中的原始模板、研究者公開的程式版本，以及本庫中文導讀分開標示；中文導讀沒有替原文補造未公開的部分。
