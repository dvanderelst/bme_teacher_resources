--- Turn links to bundled files into absolute URLs.
---
--- Handouts, media and mBlock programs are written in the source as relative
--- links -- files/Rules_for_Kinesis.docx -- which is right for the source and
--- useless everywhere else. Both of the things we ship are read away from the
--- repository: the PDF gets downloaded and printed, and the HTML is a single
--- self-contained file people save. A relative link resolves to nothing in
--- either. So both outputs get the full URL into the public repository.
---
--- The base comes from BME_FILE_BASE, set in build.sh. If it is not set the
--- links are left alone, so an ad-hoc pandoc run beside the content directory
--- still works.

local BASE = os.getenv('BME_FILE_BASE')

if not BASE or BASE == '' then return {} end

return {
  {
    Link = function (el)
      local rel = el.target:match '^(files/.+)$'
      if rel then
        el.target = BASE .. rel
        return el
      end
    end,
  },
}
