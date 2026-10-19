# GitHub 复现包归档操作手册（中文）

本文件说明如何将本项目复现包上传至 GitHub，并使稿件「Data availability」章节指向实名仓库 URL。适用于单作者、纯二次分析（公共数据再分析）的项目。

## 0. 前置条件
- 已安装 `git` 与 `gh` CLI，且已登录目标账号（`gh auth login`，账号应为 `yyx-4113`）。
- 本目录已含：README.md、CITATION.cff、LICENSE、MANIFEST.json、analysis/、manuscript/。

## 1. 本地初始化（仅在首次）
```bash
git init
git branch -M main
git config user.name  "Yongxin Yang"
git config user.email "960856791@qq.com"
```

## 2. 暂存与提交
```bash
git add -A
git status          # 确认 .workbuddy/ 已被忽略、无大体积无关文件
git commit -m "Initial deposit: pre-registered reanalysis of GSE342782 (Layer 1)"
```

## 3. 创建远程仓库并推送
```bash
gh repo create yyx-4113/mechano-phn-gse342782-reanalysis \
  --public \
  --source . \
  --remote origin \
  --push \
  --description "Pre-registered reanalysis of GSE342782: route-dependent ion-channel programmes in human sensory neurons (mechano-stress × PHN)"
```

## 4. 打版本标签（与 manuscript 版本号一致）
```bash
git tag -a v1.0.0 -m "Layer 1 pre-registered reanalysis, manuscript v1.0.0"
git push origin v1.0.0
```
推送 tag 会自动触发 `.github/workflows/release.yml`，生成带产物的 GitHub Release。

## 5. 回填稿件 Data availability
将稿件中占位行改为：
```
Reproducibility package: https://github.com/yyx-4113/mechano-phn-gse342782-reanalysis (tag v1.0.0)
```
MANIFEST.json 含全部产物的 SHA-256，可独立校验。

## 6. 后续版本
- 修订稿件后，递增版本号（v1.0.1 / v1.1.0 …），重复步骤 2、4，并同步 manuscript 与 CITATION.cff 的 version 字段。
- 冻结的 MTP panel（analysis/config/mtp_panel.json）**分析前即固定**；任何事后增改须在 commit message 与 CHANGELOG 中显式记录。
