# Folder layout and consistency checks

2026-10-26 · [Current index](../README.md) · [Source register](../course-map.md)

## Completed

- At the folder-cleanup check, root contained README.md, build-method.md and
  course-map.md. The subsequent requested teaching guide adds teaching-strategy.md;
  it is a core implementation document alongside those three files.
- Six theme folders each contain canon.md and rubric.md; comparisons and verification
  have dedicated folders.
- All 10 files in old/ match the pre-cleanup hashes byte for byte, including
  README and manifest. The manifest's eight original document hashes also match.
- Source register has 36 unique topic IDs with direct anchors and six current-system
  destinations. Four local mechanism indexes retain all 36 IDs and link to this
  register; copied PDF-page columns were removed.
- Exact PDF-page fragment links occur only in course-map.md among current files;
  mapped pages are within the known lecture page counts.
- All six current rubrics share weights 25/25/15/15/10/10 and the same unscored
  assessment status. Prior light/shadow scores are preserved in history.md.
- All six canons' numerical anchor sections and fenced code blocks are unchanged
  from the pre-cleanup files.
- 385 current local links/fragments resolve; 7 Mermaid graphs pass
  directed reachability checks. Historical snapshot links are excluded deliberately.

## Limits

This is an organization and documentation check. Mathematical experiments/tests were
not repeated because the numerical model sections are unchanged. Graphs were not
rendered; no physical demonstration, independent review, accessibility inspection,
book build, or learner trial occurred. The earlier [rebuild record](rebuild.md)
reports prior calculation checks; [history](history.md) records development decisions.

Old snapshot links reflect earlier locations and may be stale. The current index
is the entry point for live systems; immutable history is not repaired in place.

## Subsequent content development

The unchanged-numerical-sections result above applies to the folder-cleanup pass.
The later knitting/crochet strengthening intentionally extends that canon and
adds `systems/knitting-crochet/figures/repeat-panel.svg`; the theme folder now owns
its figure asset as well as canon.md and rubric.md. See the separate
[craft-centered verification](knitting-strengthening.md) for those newer checks.
