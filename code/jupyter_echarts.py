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
    option = {"title":{"text":"Distribution of Electricity","subtext":"Fake Data"},"tooltip":{"trigger":"axis","axisPointer":{"type":"cross"}},"toolbox":{"show":True,"feature":{"saveAsImage":{}}},"xAxis":{"type":"category","boundaryGap":False,"data":["00:00","01:15","02:30","03:45","05:00","06:15","07:30","08:45","10:00","11:15","12:30","13:45","15:00","16:15","17:30","18:45","20:00","21:15","22:30","23:45"]},"yAxis":{"type":"value","axisLabel":{"formatter":"{value} W"},"axisPointer":{"snap":True}},"visualMap":{"show":False,"dimension":0,"pieces":[{"lte":6,"color":"green"},{"gt":6,"lte":8,"color":"red"},{"gt":8,"lte":14,"color":"green"},{"gt":14,"lte":17,"color":"red"},{"gt":17,"color":"green"}]},"series":[{"name":"Electricity","type":"line","smooth":True,"data":[300,280,250,260,270,300,550,500,400,390,380,390,400,500,600,750,800,700,600,400],"markArea":{"itemStyle":{"color":"rgba(255, 173, 177, 0.4)"},"data":[[{"name":"Morning Peak","xAxis":"07:30"},{"xAxis":"10:00"}],[{"name":"Evening Peak","xAxis":"17:30"},{"xAxis":"21:15"}]]}}]}
    display(_echarts(option))