"""Use echarts in jupyter!"""

ECHARTS_CDN = "https://cdn.jsdelivr.net/npm/echarts@5.3.2/dist/echarts.min"
ECHARTS_REQUIREJS_CONF = f"requirejs.config({{paths: {{echarts: '{ECHARTS_CDN}',}}}});"
ECHARTS_TEMPLATE = f"""
    <div id="{{ID}}" style="width: {{WIDTH}};height:{{HEIGHT}};"></div>
    <script type="module">
    {ECHARTS_REQUIREJS_CONF}    
    requirejs(["echarts"], (echarts) => {{
                    let myChart = echarts.init(document.getElementById('{{ID}}'));
                    myChart.setOption({{OPTION}});
            }}
        )
    </script>
"""


def _multi_replace(string: str, replacements: dict):
    for k, v in replacements.items():
        string = string.replace(k, v)
    return string


def _echarts(option: dict, width="800px", height="500px"):
    import json
    from IPython.display import HTML

    option = json.dumps(option)
    # generate a random string id
    import random
    import string
    id = "".join(random.choices(string.ascii_letters + string.digits, k=10))

    h = _multi_replace(
        ECHARTS_TEMPLATE, {"{WIDTH}": width, "{HEIGHT}": height, "{OPTION}": option, "{ID}": id}
    )

    return HTML(h)

def echarts_display(option):
    from IPython.display import display
    display(_echarts(option))