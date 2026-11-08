# Materials Science StudyVault

[Download the StudyVault ZIP](https://github.com/chisomchristianu/study/raw/refs/heads/main/Materials-Science-StudyVault.zip)

Extract the ZIP, open `StudyVault` as an Obsidian vault, and start with `00-Dashboard/Study Map.md`.

Contains 26 concept notes, 40 practice questions with foldable answers, a quick reference, exam traps, source mapping and a learning dashboard. Based on [Christian Willberg's lecture 1](https://cwillberg.github.io/Lectures/stream_material_science/stream_wst_01/). Source references and supplemental explanations are identified in the notes; see Source Map for extraction limitations. Notes are study aids, not design allowables or current legal guidance.

## Updating the download

After editing the notes, run:

```sh
python scripts/package_vault.py
```

Commit the updated notes and ZIP together to update the download link above.

GitHub Actions also builds a fresh ZIP whenever notes change on main. Open the latest successful **Package StudyVault** run under **Actions**, then download its artifact (GitHub login required). Artifacts are retained for 90 days. This workflow does not update the committed ZIP automatically; its artifact always reflects that run's commit.
