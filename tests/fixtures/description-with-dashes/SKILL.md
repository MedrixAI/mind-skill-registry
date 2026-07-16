---
name: description-with-dashes
description: "a---b---c"
license: MIT
metadata:
  mind.id: ai.medrix.skill.dash-desc
  mind.distribution: builtin
---

# description-with-dashes

The description value contains the bare substring `---` which the old
`text.split("---", 2)` parser mis-split on, truncating the frontmatter.
The delimiter-line regex parser must keep this intact.
