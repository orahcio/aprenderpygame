---
title: Introducing presenterm
author: Matias
---

Introduction slide
---

An introduction slide can be defined by using a front matter at the beginning of the markdown file:

```yaml
---
title: My presentation title
sub_title: An optional subtitle
author: Your name which will appear somewhere in the bottom
---
```

The slide's theme can also be configured in the front matter:

```yaml
---
theme:
  # Specify it by name for built-in themes
  name: my-favorite-theme

  # Otherwise specify the path for it
  path: /home/myself/themes/epic.yaml

  # Or override parts of the theme right here
  override:
    default:
      colors:
        foreground: white
---
```

<!-- end_slide -->

Headers
---

Using commonmark setext headers allows you to set titles for your slides (like seen above!):

```
Headers
---
```

# Other headers

All other header types are simply treated as headers within your slide.

## Subheaders
### And more

<!-- end_slide -->

Slide commands
---

Certain commands in the form of HTML comments can be used:

# Ending slides

In order to end a single slide, use:

```html
<!-- end_slide -->
```

# Creating pauses

Slides can be paused by using the `pause` command:

```html
<!-- pause -->
```

This allows you to:

<!-- pause -->
* Create suspense.
<!-- pause -->
* Have more interactive presentations.
<!-- pause -->
* Possibly more!

<!-- end_slide -->

Code highlighting
---

Code highlighting is enabled for code blocks that include the most commonly used programming languages:

```rust
// Rust
fn greet() -> &'static str {
    "hi mom"
}
```

```python
# Python
def greet() -> str:
    return "hi mom"
```

```cpp
// C++
string greet() {
    return "hi mom";
}
```

And many more!

<!-- end_slide -->

Dynamic code highlighting
---

Select specific subsets of lines to be highlighted dynamically as you move to the next slide. Optionally enable line 
numbers to make it easier to specify which lines you're referring to!

```rust {1-4|6-10|all} +line_numbers
#[derive(Clone, Debug)]
struct Person {
    name: String,
}

impl Person {
    fn say_hello(&self) {
        println!("hello, I'm {}", self.name)
    }
}
```

<!-- end_slide -->

Shell code execution
---

Run commands from the presentation and display their output dynamically.

```bash +exec
for i in $(seq 1 5)
do
    echo "hi $i"
    sleep 0.5
done
```