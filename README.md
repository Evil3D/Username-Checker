## Why this tool exists

I originally wanted a simple username lookup tool.
If you search *“username lookup”*, the top result is [**Instant Username Search**](https://instantusername.com), which at first glance looks clean and reliable.

Then I read their [Terms of Service](https://instantusername.com/terms) — which explicitly state that they are **not liable for incorrect results**. That alone isn’t a dealbreaker, but it made me curious enough to inspect how their checks actually work.

The Roblox checker was the breaking point.

Their lookup links to:

```
https://www.roblox.com/user.aspx?username=<username>
```

This endpoint returns the **same response** for:

* available usernames
* terminated usernames
* certain invalid usernames

In other words:
**it cannot distinguish between “claimable” and “not claimable”.**

As a result, the tool effectively reports **every username as taken**, regardless of reality. That isn’t unreliable - it’s structurally incorrect.

---

## Why profile lookup is the wrong approach

Profile-based username checks are fundamentally flawed because:

* Websites can (and do) return false responses when they detect scraping
* Profile pages often return identical responses for multiple states
* Existence ≠ availability (terminated, reserved, blocked, etc.)
* You cannot verify whether the site is telling the truth

If an endpoint cannot *theoretically* differentiate between states, no amount of retries or proxying will fix that.

---

## Why this tool uses signup APIs instead

This tool uses **signup / username validation APIs** wherever possible, because:

1. **They are more reliable than profile lookup**
2. **They are authoritative**

Signup APIs are constrained by a hard requirement:

> They cannot lie consistently without breaking account creation.

If a signup API falsely reports usernames as available or unavailable:

* either everyone could claim any username
* or nobody could sign up at all

Both outcomes would make the signup system unusable.

So when a signup API gives a definitive answer, that answer is real.

If a signup check fails, that’s not treated as “unknown” or guessed - it’s treated as **unavailable**, and the endpoint gets investigated or fixed later.

---

## Design philosophy

* Only return **“yes”** when the platform explicitly confirms availability
* Everything else is **“no”**
* No guessing
* No smoothing
* No profile scraping unless there is *literally no alternative*
* If an API changes and breaks, it gets fixed - not hidden

This tool prioritizes **truth over UX**, even if that means fewer “yes” results.

---

## Contributing

If you find:
- a broken check
- incorrect behavior
- a better API approach

please open a GitHub issue or submit a pull request. Contributions are welcome.
