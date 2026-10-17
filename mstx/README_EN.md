<h1 align="center">MindStudio Tools Extension Library</h1>

<div align="center">
<p><b><span style="font-size:24px;">Ascend AI Operator Tool Extension Interface Library</span></b></p>

 [![AI Q&A (DeepWiki)](https://badgen.net/badge/AI%20Q%26A/DeepWiki/blue)](https://deepwiki.com/mindstudio-docs/26.2.0)
 [![AI Q&A (ZRead)](https://badgen.net/badge/AI%20Q%26A/ZRead/blue)](https://zread.ai/mindstudio-docs/26.2.0)
 [![Exact Search](https://badgen.net/badge/Exact%20Search/ReadTheDocs/blue)](https://mindstudio-operator-tools-docs.readthedocs.io/zh-cn/latest/)
 [![Ascend Community](https://badgen.net/badge/Ascend%20Community/Community/blue)](https://www.hiascend.com/en/developer/software/mindstudio)
 [![Report Issues](https://badgen.net/badge/Report%20Issues/Issues/blue)](https://atomgit.com/Ascend/mstx/issues)

</div>

English | [简体中文](./README.md)

## ✨ What's New

<span style="font-size:14px;">

🔹 **[Dec 31, 2025]**: The MindStudio Tools Extension Library project is now fully open source.

</span>

## ℹ️ Introduction

MindStudio Tools Extension Library (msTX) introduces the msTX instrumentation API. It allows you to customize collection time ranges or the start and end time points of key functions, identify information such as key functions or iterations, and quickly scope performance and operator issues.

## ⚙️ Features

By default, the mstx API has no functionality. You need to call the mstx API in your user application and then enable the mstx instrumentation feature for different scenarios, such as configuring `--mstx=on` when profiling data with the msprof CLI, configuring `ACL_PROF_MSPROFTX` when profiling data with the AscendCL API, and configuring `mstx=True` when profiling data with the Ascend PyTorch Profiler API.

## 🌌 Smart Search

To improve documentation search efficiency, we provide multiple efficient search methods:  
🔹 [AI Q&A (DeepWiki)](https://deepwiki.com/mindstudio-docs/26.2.0): Natural language Q&A to quickly grasp the project architecture and module relationships.   
🔹 [AI Q&A (ZRead)](https://zread.ai/mindstudio-docs/26.2.0): Better Chinese Q&A experience for precisely locating feature usage and details.   
🔹 [Precise Search (ReadTheDocs)](https://mindstudio-operator-tools-docs.readthedocs.io/zh-cn/latest/): Full-text keyword search that takes you directly to APIs, parameters, error messages, and more.  

## 📦 Installation Guide

For environment dependencies and installation methods, see the [msTX Installation Guide](docs/en/install_guide/mstx_install_guide.md).

## 💡 Typical Use Cases

For typical usage scenarios, refer to [msOpProf Extended Functions](https://atomgit.com/Ascend/msopprof/blob/26.2.0/docs/en/user_guide/extended_functions.md#mstx-extended-functions) and [msSanitizer API Reference](https://atomgit.com/Ascend/mssanitizer/blob/26.2.0/docs/en/api_reference/mssanitizer_api_reference.md#mstx-functions).

## 📚 API Reference

For details on msTX APIs, refer to [msTX API Reference](docs/en/api_reference/README.md).

## 🛠️ Contribution Guide

Contributions are welcome. For details, see the [Contribution Guide](./docs/en/contributing/contributing_guide.md).

## ⚖️ Related Information

🔹 [Release Notes](https://atomgit.com/Ascend/mstx/releases)  
🔹 [LICENSE Statement](./docs/en/legal/license_notice.md)  
🔹 [Security Statement](./docs/en/legal/security_statement.md)  
🔹 [Disclaimer](./docs/en/legal/disclaimer.md)  

## 🤝 Suggestions and Communication

We welcome contributions to the community. If you have any questions or suggestions, please submit an [Issue](https://atomgit.com/Ascend/mstx/issues), and we will respond as soon as possible. Thank you for your support.

| Instant Interaction (WeChat Group) | Official Updates (Official Account) | In-Depth Support (Assistant/Forum) |
| :---: | :---: | :--- |
| <img src="https://raw.atomgit.com/Ascend/docs/files/master/common/Writing_Template/figures/qr_code_wechat_work.png" width="120"><br><sub>*Scan the QR code to join the technical exchange group.*</sub> | <img src="https://raw.atomgit.com/Ascend/docs/files/master/common/Writing_Template/figures/qr_code_wechat_official_account.png" width="120"><br><sub>*Scan the QR code to follow the official account.*</sub> | Scan the QR code to join the group and follow the official account, the fastest communication channel for MindStudio users and developers:<br> **Quick Q&A:** Discuss technical issues with community members in real time.<br>**Latest Updates:** Get notified of version releases and feature updates as soon as possible.<br> **Experience Sharing:** Exchange best practices and hands-on experience with developers.<br> <br> **More Support Channels**: 👉 Ascend Assistant: [![WeChat](https://img.shields.io/badge/WeChat-07C160?style=flat-square&logo=wechat&logoColor=white)](https://atomgit.com/Ascend/msit/blob/master/docs/zh/figures/readme/xiaozhushou.png) 👉 Ascend Forum: [![Website](https://img.shields.io/badge/Website-%231e37ff?style=flat-square&logo=RSS&logoColor=white)](https://www.hiascend.com/forum/) |

## 🙏 Acknowledgments

This tool is jointly contributed by Huawei Technologies Co., Ltd. and developers.

Thanks for every PR from the community, and contributions are welcome.
