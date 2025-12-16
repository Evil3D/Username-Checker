# Username Checker

A username availability checker that focuses on correctness over guesswork.

This project checks whether a username is actually usable for signup on supported platforms. Unlike many existing tools, it does **not** rely solely on profile lookups,
which are often unreliable.

---

## Why this exists

This project was mainly inspired by how inaccurate some username checkers are
(e.g. [Instant Username](https://instantusername.com)).

Many of them determine availability by checking whether a public profile exists.
That approach breaks down on platforms where:
- terminated accounts exist
- usernames are reserved
- profile endpoints return the same response for multiple states

### Example: Roblox

Some services check:
```https://www.roblox.com/user.aspx?username=<username>```

This endpoint returns the same `404` for:
- never-registered usernames (available)
- terminated usernames (unavailable)

As a result, taken and available usernames can be incorrectly reported (or treated
as the same state), which makes the result useless for actual signup.

---

## How this project works

Whenever possible, this project uses **actual signup / validation APIs** instead of
profile lookups.

Signup APIs generally provide much more reliable information about whether a
username can be registered.

For platforms where:
- signup APIs are unavailable, or
- validation is too complex,

a profile lookup may still be used as a fallback.

---

## Accuracy

Using signup and validation APIs is **significantly more reliable** than
profile-based checks.

These endpoints are typically designed to validate usernames during account
creation and therefore provide clearer and more accurate signals than public
profile lookups. In many cases, they are also subject to less aggressive rate
limiting than large-scale profile scraping.

However, no method is perfect. Accuracy may still be affected by:
- rate limits
- platform changes
- anti-bot or abuse prevention systems

When a definitive answer cannot be determined, the checker should return an
**uncertain** result rather than guessing.

---

## Scope & Limitations

This project is **not intended for large-scale or production use**.

Checks are performed on a best-effort basis, and no additional safeguards are
implemented for API failures, timeouts, or unexpected responses. If a platform’s
API fails or behaves unexpectedly, the result may be incomplete or marked as
uncertain.

This is an intentional design choice to keep the project simple and focused on
accuracy when APIs respond as expected.

If you need production-grade reliability, retries, or high-volume usage, this
project is probably not what you’re looking for.

---

## Contributing

If you find:
- a broken check
- incorrect behavior
- a better API approach

please open a GitHub issue or submit a pull request. Contributions are welcome.
