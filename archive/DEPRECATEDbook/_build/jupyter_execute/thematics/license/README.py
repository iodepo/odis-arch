#!/usr/bin/env python
# coding: utf-8

# # Licenses
# 
# 
# ## Schema.org License
# 
# - https://schema.org/license
#     - `URL`
#     - `CreativeWork`
# 
# ### License as URL - Good
# 
# <pre>
# {
#   "@context": "https://schema.org/",
#   <strong>"license": "https://creativecommons.org/licenses/by/4.0/"</strong>
# }
# </pre>
# 
# ### License as CreativeWork - Better?
# 
# <pre>
# {
#   "@context": "https://schema.org/",
#   <strong>"license": {
#     "@type": "CreativeWork",
#     "name": "Creative Commons Attribution 4.0",
#     "url": "https://creativecommons.org/licenses/by/4.0/"
#   }</strong>
# }
# </pre>
# 
# ### License as SPDX URL - Best
# 
# - Use a simple URL
# - [SPDX](https://spdx.org/licenses/) creates URLs for many licenses including those that don't have URLs
# - From a source that <em>harvesters</em> can rely on (e.g. use URL to lookup more information about the license)
# 
# <pre>
# {
#   "@context": "https://schema.org/",
#   <strong>"license": "https://spdx.org/licenses/CC-BY-4.0"</strong>
# }
# </pre>
# 
# OR, include both the SPDX and the Creative Commons URLs in an array:
# 
# <pre>
# {
#   "@context": "https://schema.org/",
#   <strong>"license": ["https://spdx.org/licenses/CC-BY-4.0", "https://creativecommons.org/licenses/by/4.0/"]</strong>
# }
# </pre>
