-- Remove HTML comments from the output.
--
-- Pandoc already drops raw HTML when producing LaTeX, so revision notes cannot
-- reach the PDF. They would, however, survive into the HTML *source*, where
-- anyone viewing source on the published site could read them. Strip them.
local function is_comment(el)
  return el.format == "html" and el.text:match("^%s*<!%-%-")
end

return {
  { RawBlock  = function(el) if is_comment(el) then return {} end end,
    RawInline = function(el) if is_comment(el) then return {} end end },
}
