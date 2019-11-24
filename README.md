# `make-story`

This is a utility project designed to streamline the process of converting document sets into another filetype. While the inspiration for creating this utility is my own writing, my goal is to create a utility that can be used to create any document type available by the specified converter. By default, `make-story` uses `pandoc` for conversion, but later versions will allow this to be changed via configuration files or command-line options.

## Contributing

### Commit Messages

The semantics for commit messages is

```
<TYPE> [scope]: <brief description>
<BLANK>
[body]
<BLANK>
[footer]
```

**Version-Changing Commit Types:**

These changes affect production code _and_ version control.

- `FIX` -- Fixes a bug (PATCH version)
- `FEAT` -- Adds a new feature (MINOR version)

**Production Code Commit Types:**

These commits affect production code _without_ affecting version control.

- `PERF` -- Improves performance of a given feature
- `REFACTOR` -- Code refactoring

**Other Commit Types:**

These commits do not affect production code, nor do they affect version control.

- `CHORE` -- Updating configuration, tasks, etc
- `DOC` -- Adds or modifies documentation
- `TEST` -- Adds or refactors tests

**Handling Breaking Changes:**

These changes are recorded in the body or footer of the commit message. They may or may not affect production code or version control.

- `BREAKS` -- Should be immediately followed by a description of what it's breaking (changes MAJOR version)
- `REVERTS` -- Should be immediately followed by the commit being reverted (changes based on commit type)
