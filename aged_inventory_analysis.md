# GEE Automotive Portland - Aged Inventory Analysis
## Analysis Date: January 6, 2026

## Data Processing

From the inventory screenshot, I can identify:

### Sample of Aged Units Visible:

**High Priority (150+ days):**

1. **VIN: ZDMH4TPS5SB004818** - SCRAMBLER ICON
   - Invoice: 2025-06-27
   - Days: ~193 days
   - Model: SCRAMBLER 25 CAL NMR CRB STD DMH

2. **VIN: ZDSH514T5...** (need full VIN from column)
   - Invoice: 2025-06-30
   - Days: ~190 days
   - Model: Multiple Scrambler units visible

3. **Additional aged units** - Need to parse full spreadsheet

### Issue Identified:

I need to:
1. Extract ALL actual VINs from the "equipment" column
2. Calculate exact days in stock from invoice dates
3. Create full Excel attachment with:
   - VIN (full)
   - Model
   - Invoice Date
   - Days in Stock
   - Applicable Incentive
   - Priority Level

### Next Step:

User needs to provide the data in a format I can parse properly (Excel file upload or CSV), or I can create a template showing what the attachment should look like based on the visible data.
