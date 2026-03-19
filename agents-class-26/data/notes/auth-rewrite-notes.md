# Auth Service Rewrite — Notes

## Problem
Session tokens validated on every request → hitting DB each time → latency spike at peak (p99 ~200ms).

## Solution
- Cache token validation results in Redis (TTL = token expiry - 30s)
- Redesign refresh flow to use sliding window expiry
- Remove legacy MD5 token generation (security issue flagged in last audit)

## Key decisions
- Chose Redis over Memcached: team already has ops expertise, cluster replication built in
- Sliding window: token TTL resets on activity, hard cap at 30 days
- Revocation list stored in Redis sorted set (score = expiry timestamp)

## Performance results (staging)
| Metric        | Before   | After   |
|---------------|----------|---------|
| p50 latency   | 18ms     | 3ms     |
| p99 latency   | 200ms    | 12ms    |
| Cache hit rate | —       | 94%     |

## Follow-up tickets
- [ ] #861 — Refresh token revocation endpoint
- [ ] #862 — Rate limiting on /auth/refresh
- [ ] #863 — Audit log for token operations
