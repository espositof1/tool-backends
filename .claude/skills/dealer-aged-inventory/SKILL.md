---
name: dealer-aged-inventory
description: Identifies which dealer inventory units require immediate sales focus based on aging and concentration, and safely aligns them with current Ducati sales incentives. Use for monthly dealer inventory reviews, VIN prioritization, and supportive dealer communications. Never use for pricing recommendations, enforcement, or customer-facing content.
---

# Dealer Aged Inventory Focus & Incentive Alignment

**Domain**: Automotive OEM Sales Operations
**Version**: 1.0.0
**Confidence Level**: High

## Mission

This Skill exists to proactively steer dealer focus toward aged inventory before flooring cost and imbalance become a problem — without creating panic or credibility risk.

**Success looks like:**
- Dealers clearly understand which units to focus on this month
- Sales Managers can act immediately using correct, current incentives
- Communication feels supportive, premium, and precise

## Intended Use

✅ **Use for:**
- Monthly identification of aged dealer inventory requiring proactive sales focus
- Dealer-facing prioritization of models and VINs to act on now
- Creating supportive, actionable dealer communications

❌ **Never use for:**
- Pricing or discount recommendations
- Dealer enforcement or compliance monitoring
- Customer-facing communication

---

## Domain Assumptions

**The Skill assumes:**
- Inventory data includes VIN, model, dealer, and invoice date
- Units aged 90+ days are at risk of incurring flooring interest
- Sales incentives are provided via an official monthly bulletin
- Seasonality materially affects urgency and tone

**The Skill does NOT assume:**
- Whether a unit came from allocation vs open order
- That incentives guarantee sell-through
- That dealers want or should discount inventory

---

## Signal Hierarchy (Most → Least Important)

### 1. Age in Days Since Invoice
- **Primary risk signal**
- Determines urgency tier
- Always takes precedence

### 2. Model Concentration at Dealer
- ≥3 units of same model = attention required
- High concentration + aging = compounded risk

### 3. Seasonality (Tone Modifier)
- Q1: opportunity framing
- Apr–Jul: reminder / north-star focus
- Late Q3–Q4: priority action framing

### 4. Available Incentives (Support, not pressure)
- Used to enable action
- Never overstated or inferred

**Explicitly ignored signals:**
- Color / trim
- MSRP differences
- National sales noise
- Small age deltas (e.g., 92 vs 100 days)

---

## Decision Rules (Explicit Logic)

### 1. Aging Classification

**90–120 days**
- Status: "Begin focusing"
- Tone: Light, informative
- Urgency: Low-medium

**120–150 days**
- Status: "Needs attention"
- Tone: Clear, action-oriented
- Urgency: Medium-high

**150+ days**
- Status: "Primary focus now"
- Tone: Direct, prioritized
- Urgency: High

### 2. Model Concentration Rule

```
IF dealer has ≥ 3 units of the same model
AND any of those units are ≥ 90 days
THEN model must be highlighted
```

⚠️ High volume dealers are not exempt — age + clustering always matters.

### 3. Seasonality Tone Adjustment

**Q1 (Jan–Mar)**
- Emphasize opportunity to prepare for peak season
- Language: "strong opportunity," "season build-up"

**Apr–Jul (Peak Retail)**
- Soft reminder; act as "north star" amid high traffic
- Language: "continue focus," "maintain momentum"

**Late Q3–Q4**
- Emphasize urgency to retail while season allows
- Language: "prioritize now," "take action"

⚠️ **Seasonality never suppresses aged-unit visibility** — it only adjusts language.

### 4. Incentive Alignment Rule (CRITICAL)

```
ONLY reference incentives explicitly listed
in the uploaded official sales bulletin

- No inference
- No extrapolation
- No "best guess"
```

**If uncertainty exists → flag for verification**

---

## Failure Prevention (Hard Stops)

The Skill MUST NEVER:

❌ Recommend discounting
❌ Create panic or anxiety
❌ Sound like enforcement or blame
❌ Suggest incorrect or inapplicable incentives
❌ Include raw data dumps in email body

**Safety Rule:**
If incentive applicability is unclear → Downgrade confidence and instruct verification before customer discussion.

---

## Output Rules (Dealer-Facing Email)

**Attention span target**: 30 seconds initial read

### Structure

1. **Short intro (2–3 lines)**
   - Purpose: proactive inventory support
   - Friendly, premium tone

2. **Top 2–3 VINs only**
   - Most aged
   - Model-representative
   - High impact

3. **Model-level focus summary**
   - "X units of Multistrada family currently aged"
   - Brief context without overwhelming

4. **Incentive recap (high-level)**
   - Financing / cash support
   - No fine print
   - Easy to understand

5. **CTA**
   - "Full VIN-level recap attached for immediate use"
   - Clear next action

### Length & Tone

- **Extremely concise**
- **Premium, confident, supportive tone**
- Never blame or pressure
- Always actionable

---

## Output Format Examples

### Example 1: Q1 Opportunity Framing

**Subject:** Dealer Focus – January Inventory Review

**Body:**
```
VIN XXXXX – Multistrada V4
In stock 152 days
Current support: 0% / 36 mo or $2,500 cash bonus

VIN YYYYY – Multistrada V4
In stock 128 days
Same support applies

We currently have 7 Multistrada units in stock.
As we enter the season build-up, this is a strong opportunity
to prioritize these models with available Ducati support.

➡️ Full VIN-level recap attached for your sales team.
```

### Example 2: Late Q3 Priority Action

**Subject:** Priority Inventory Focus – September

**Body:**
```
VIN ZZZZZ – Scrambler Icon
In stock 168 days
Current support: 0% / 48 mo or $1,500 cash bonus

VIN AAAAA – Scrambler Icon
In stock 145 days
Same support applies

With 5 Scrambler units currently aged, now is the time to
prioritize these models while the season allows strong retail activity.

➡️ Full VIN-level recap attached for immediate action.
```

### Example 3: Incentive Uncertainty Flag

**Body includes:**
```
⚠️ Note: Please verify incentive applicability with your regional
sales manager before customer discussions.
```

---

## Expected Inputs

When using this Skill, provide:

1. **Inventory data** with:
   - VIN
   - Model name
   - Dealer name
   - Invoice date (or days since invoice)

2. **Current month/quarter** for seasonality adjustment

3. **Official sales incentive bulletin** (uploaded or referenced)

---

## Self-Check Criteria

Before finalizing output, verify:

✅ Did I prioritize age and model concentration correctly?
✅ Did I avoid panic and enforcement language?
✅ Did I reference incentives only from the bulletin?
✅ Did I keep the output short enough to act on?
✅ Would a senior OEM sales leader sign this email?

**Final Quality Check:**

✅ Encodes expert judgment
✅ Reduces cognitive load
✅ Protects brand & credibility
✅ Drives immediate dealer action

❌ Not a template
❌ Not generic reporting

---

## Edge Cases & Handling

**Edge Case 1: Aged unit during peak season (April)**
- Still flag the unit
- Use softer reminder framing
- Emphasize "maintain focus" rather than urgency

**Edge Case 2: Incentive not clearly applicable**
- Flag: "verify before customer communication"
- Lower confidence
- Provide context but no false certainty

**Edge Case 3: Small dealer with only 2 aged units**
- Still highlight if 120+ days
- Adjust tone to be supportive, not alarming
- Focus on opportunity, not problem

**Edge Case 4: High-volume dealer with many aged units**
- Prioritize top 2-3 VINs only in email
- Reference total count
- Attach full list
- Do not overwhelm

---

## Implementation Notes

**Good Input → Good Output:**
- Dealer with 5 units of same model
- 2 units aged 160+ days
- Incentive explicitly listed in bulletin
→ Highlights model + 2 VINs + correct incentive

**Bad Input → Corrected Output:**
- Incentive not clearly applicable
→ Flags "verify before customer communication"

**Seasonal Edge Case:**
- Aged unit in April
→ Still flagged, softer tone, reminder framing

---

## Quality Assurance

This Skill is designed to:

✅ **Protect credibility** — Never overstate or guess incentives
✅ **Drive action** — Clear, immediate next steps
✅ **Maintain premium brand** — Supportive, not enforcement
✅ **Scale expertise** — Encode senior sales leader judgment

Use this Skill monthly for proactive dealer inventory management that supports sales performance without creating unnecessary pressure.
