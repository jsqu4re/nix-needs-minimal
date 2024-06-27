"""sphinx configuration file"""

import os

# -- Environment Variables to be set by NIX --------------------------------

DOCS_NAME = os.getenv("DOCS_NAME", "nix-needs-minimal")
DOCS_AUTHOR = os.getenv("DOCS_AUTOR", "the author")
DOCS_VERSION = os.getenv("DOCS_VERSION", "0.1.0")
DOCS_COPYRIGHT_OWNER = os.getenv("DOCS_COPYRIGHT_OWNER", "copyright owner")
DOCS_COPYRIGHT_BEGIN = os.getenv("DOCS_COPYRIGHT_BEGIN", "2024")
DOCS_COPYRIGHT_END = os.getenv("DOCS_COPYRIGHT_END", "2024")

# --------------------------------------------------------------------------


# General documentation information

project = DOCS_NAME
copyright = f"{DOCS_COPYRIGHT_BEGIN}-{DOCS_COPYRIGHT_END}, {DOCS_COPYRIGHT_OWNER}"
author = DOCS_AUTHOR

language = "en"

version = DOCS_VERSION

extensions = [
    "sphinxcontrib.plantuml",
    "sphinx_needs",
    "sphinx_design",
    "sphinx_immaterial",
]

master_doc = "index"

exclude_patterns = ["out", "result"]

# -- Options for html builder ----------------------------------------------

html_static_path = ["_static"]
html_css_files = ["_css/shared.css"]
html_favicon = "./_static/sphinx-needs-card.png"

# https://jbms.github.io/sphinx-immaterial
html_theme = "sphinx_immaterial"

html_logo = "./_static/sphinx-needs-card.png"
templates_path = ["_templates/sphinx_immaterial"]
html_css_files += ["_css/sphinx_immaterial.css"]
html_sidebars = {
    "**": ["about.html", "navigation.html", "searchbox.html"],
}
html_theme_options = {
    "font": False,
    "icon": {
        "repo": "fontawesome/brands/github",
    },
    "site_url": "https://jsqu4re.github.io/nix-needs-minimal/",
    "repo_url": "https://github.com/jsqu4re/nix-needs-minimal",
    "repo_name": "Nix-Needs-Minimal",
    "edit_uri": "blob/master/docs",
    "globaltoc_collapse": True,
    "features": [
        "navigation.sections",
        "navigation.top",
        "search.share",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "blue",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/weather-night",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "blue",
            "accent": "yellow",
            "toggle": {
                "icon": "material/weather-sunny",
                "name": "Switch to light mode",
            },
        },
    ],
    "toc_title_is_page_title": True,
}

# -- Options for PlantUML extension ----------------------------------------

plantuml = f"plantuml"

# plantuml_output_format = 'png'
plantuml_output_format = "svg_img"

# -- Options for Needs extension -------------------------------------------

needs_debug_measurement = False

needs_types = [
    {
        "directive": "node",
        "title": "Need Node",
        "content": "plantuml",
        "prefix": "N_",
        "color": "#BFD8D2",
        "style": "card",
    },
]

needs_extra_links = [
    {
        "option": "blocks",
        "incoming": "is blocked by",
        "outgoing": "blocks",
        "copy": True,
        "style": "#AA0000",
        "style_part": "dotted,#AA0000",
        "style_start": "-",
        "style_end": "-o",
        "allow_dead_links": True,
    },
]

needs_show_link_type = False
needs_show_link_title = False
needs_title_optional = True
needs_max_title_length = 75

needs_id_regex = "^[A-Za-z0-9_]*"
needs_id_required = True

needs_table_style = "datatables"
needs_table_columns = "ID;TITLE;STATUS;OUTGOING"

needs_extra_options = [
    "my_extra_option",
    "another_option",
    "author",
    "comment",
]

needs_warnings = { }

needs_default_layout = "clean"
needs_default_style = None

needs_service_all_data = True

needs_services = {}

needs_build_json = True
needs_build_json_per_id = False

NOTE_TEMPLATE = """
.. _{{id}}:

.. note:: {{title}} ({{id}})

   {{content|indent(4) }}

   {% if status -%}
   **status**: {{status}}
   {% endif %}

   {% if tags -%}
   **tags**: {{"; ".join(tags)}}
   {% endif %}

   {% if links -%}
   **links**:
   {% for link in links -%}
       :ref:`{{link}} <{{link}}>` {%if loop.index < links|length -%}; {% endif -%}
   {% endfor -%}
   {% endif %}
"""

DEFAULT_DIAGRAM_TEMPLATE = "<size:12>{{type_name}}</size>\\n**{{title|wordwrap(15, wrapstring='**\\\\n**')}}**\\n<size:10>{{id}}</size>"
