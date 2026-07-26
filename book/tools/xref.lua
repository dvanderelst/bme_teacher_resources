--- Follow every internal cross-reference with the page it points to.
---
--- These materials are meant to be printable, and a printed cross-reference that
--- says only "see Resetting the firmware" is useless: there is nothing to click
--- and no page to turn to. So in the PDF each internal link gains a page
--- reference, giving "see Resetting the firmware (on page 14)".
---
--- varioref rather than a plain \pageref, because it phrases the common cases
--- the way a book does -- "on this page", "on the next page", "on the preceding
--- page" -- and only falls back to a number when the target is further away.
---
--- LaTeX only. In HTML the link is live, so a page number would be meaningless.
--- The heading anchors pandoc generates double as LaTeX \labels, which is what
--- makes this work without labelling anything by hand.

if not FORMAT:match 'latex' then return {} end

return {
  {
    Link = function (el)
      local anchor = el.target:match '^#(.+)$'
      if not anchor then return nil end
      -- A link to a figure gets its number as well as its page. LaTeX counts the
      -- figures itself, so the number cannot drift as the book is edited.
      local macro = anchor:match '^fig:' and '\\figref{' or '\\pageofref{'
      return {
        el,
        pandoc.RawInline('latex', macro .. anchor .. '}'),
      }
    end,
  },
}
