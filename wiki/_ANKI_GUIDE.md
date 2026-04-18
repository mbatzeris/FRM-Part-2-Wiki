# Anki Quickstart Guide — FRM Part 2

A minimal-setup guide to get your R30 cards loaded and start reviewing today. Total setup time: ~5 minutes.

---

## 1. Create Your Deck

1. Open Anki on your PC.
2. Click **Create Deck** (bottom of main screen).
3. Name it: `FRM Part 2 — Credit Risk` (or just `FRM Part 2` if you prefer one deck for everything).
4. Press **OK**.

## 2. Import the R30 Cards

1. Go to **File → Import...** (top menu bar).
2. Browse to: `wiki\Book 2 - Credit Risk\R30_anki_cards.txt`
3. Anki will show the import settings screen. Verify:
   - **Type:** `Basic`
   - **Deck:** `FRM Part 2 — Credit Risk` (select the one you just created)
   - **Field separator:** `Tab` (should auto-detect)
   - **Field 1 mapped to:** `Front`
   - **Field 2 mapped to:** `Back`
   - **Allow HTML in fields:** checked (optional, won't hurt)
   - **Existing notes:** `Update` or `Import as new`
4. Click **Import**.
5. You should see: **"30 notes imported."**

## 3. Start Reviewing

1. Back on the main screen, click your `FRM Part 2 — Credit Risk` deck.
2. Click **Study Now**.
3. A card front appears. **Try to answer in your head** (or out loud — better for memory).
4. Click **Show Answer**.
5. Rate yourself honestly:
   - **Again** (red) — "I had no idea." Card reappears in ~1 minute.
   - **Hard** — "I sort of knew it but struggled." Card reappears in ~10 minutes.
   - **Good** (green) — "I got it right." Next review in ~1 day.
   - **Easy** — "This was trivial." Next review in ~4 days.

**Rule of thumb:** If you hesitated more than 5 seconds, press **Hard** or **Again**. Anki's algorithm works best with honest self-grading.

## 4. Recommended Settings (one-time)

Click the **gear icon** next to your deck name → **Options**:

| Setting | Recommended Value | Why |
|:--|:--:|:--|
| **New cards/day** | 10 | Spread the 30 cards over 3 days to avoid overwhelm |
| **Maximum reviews/day** | 100 | Won't hit this early; ensures no cap when cards accumulate |
| **Learning steps** | 1m 10m | Default is fine; cards graduate after 2 correct answers |
| **Graduating interval** | 1 day | First "real" review after 1 day |
| **Easy interval** | 4 days | For cards you already know cold |
| **Maximum interval** | 180 days | Caps how far apart reviews can get (~6 months) |

Leave everything else at defaults. You can fine-tune later.

## 5. Daily Routine (5 minutes)

```
Morning (phone) or lunch (PC):
  → Open Anki
  → "Study Now" on the FRM deck
  → Answer all due cards (~20-30 cards = 5 min)
  → Close
  → Done
```

That's it. Anki's algorithm handles the scheduling. You just show up.

## 6. Sync Across Devices (PC ↔ Phone)

### Create a free AnkiWeb account
1. Go to https://ankiweb.net/account/register
2. Sign up (free).

### Sync from PC
1. In Anki, click the **Sync** button (circular arrow, top right).
2. Log in with your AnkiWeb account.
3. First sync will upload everything.

### Install on phone
- **Android:** Install **AnkiDroid** (free) from Google Play.
- **iPhone:** Install **AnkiMobile** ($24.99 — the only paid option, but worth it for daily commute use).

### Sync on phone
1. Open AnkiDroid/AnkiMobile.
2. Tap **Sync** → log in with the same AnkiWeb account.
3. Your 30 cards will appear.

**Sync flow:** Always sync PC after adding new cards → phone auto-pulls them on next sync.

## 7. Adding Cards for Future Readings

Every time you complete a new `/new-reading`, I'll generate a `R{N}_anki_cards.txt` file in the same format. To import:

1. **File → Import** → select the new `.txt` file.
2. Same settings as Step 2.
3. New cards are added to the same deck. Anki deduplicates automatically (by front text).

## 8. Tags (optional, useful later)

When you have 200+ cards across multiple readings, you may want to filter by topic. To add tags during import:

1. Add a third column to the `.txt` file: `front\tback\ttags`
2. Tags can be: `R30`, `Book2`, `CVA`, etc.
3. In Anki, you can then create **Filtered Decks** or **Custom Study** sessions by tag.

I'll start including tags in future card files if you want. For now, 30 cards in one deck is simple enough.

---

## Common Questions

**Q: I missed a day. What happens?**
A: Nothing bad. Overdue cards pile up and Anki shows them next time you open it. Just do them — the algorithm self-corrects.

**Q: Should I study new cards AND review old cards?**
A: Yes, every session. Anki mixes them automatically. New cards are blue; review cards are green; overdue are red.

**Q: When do I add more cards?**
A: After each `/new-reading` — I generate the `.txt`, you import. Target: ~10-15 new cards per reading = ~800 total by November.

**Q: 800 cards sounds like a lot!**
A: By November, daily review will still be ~15-20 minutes because Anki spaces mature cards far apart. The daily load plateaus around 40-60 cards/session regardless of total deck size.

**Q: Should I edit cards?**
A: Yes! If a card is confusing or the answer doesn't match what you learned in AnalystPrep, edit it. Right-click → Edit during review, or browse all cards via **Browse** (top menu).
