from flask import Flask, request, render_template, make_response
import requests

from connConfigDto import ConnConfigDto
from VmDto import VmDto

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route("/connections", methods=['GET', 'POST'])
def connections():
    if request.method == 'POST':
        spider_url = request.form.get('spider_url')
        connections = get_connections(spider_url)

        resp = make_response(render_template("connection.html", connections=connections))
        resp.set_cookie('spider_url', spider_url)
        return resp
    else:
        return render_template("connection.html")


@app.route("/connections/<string:connectionName>", methods=['GET', 'POST'])
def connection_vm_list(connectionName):
    if request.method == 'GET':
        only_csp_list = get_vm_list(connectionName)
        return render_template("vmlist.html", only_csp_list=only_csp_list, connectionName=connectionName)
    else: # vm 등록
        vm_id = request.form.get("name_id")
        vm_system_id = request.form.get("system_id")

        # cb-spider에 vm 정보 get request
        spider_url = request.cookies.get("spider_url")




#cb-spider에 vm등록하는 함수
def regist_vm():
    reg_vpc()
    reg_subnet()
    reg_security_group()
    reg_keypair()


def reg_vpc():
    pass


def reg_subnet():
    pass


def reg_security_group():
    pass


def reg_keypair():
    pass









def get_connections(spider_url):
    response = requests.get(f"http://{spider_url}/spider/connectionconfig")
    row = response.json()

    connections = []
    for connection in row['connectionconfig']:
        connConfigDto = ConnConfigDto(connection["ConfigName"])
        connections.append(connConfigDto)

    return connections


# AllList / OnlySpiderList / OnlyCSPList => 여기에 있는 것들은 등록 안 된 것들..
# allvpc, allsequritygroup, allkeypair, allvm body{"ConnectionName : "~~~"}
def get_vm_list(connection_name):
    spider_url = request.cookies.get('spider_url')

    params ={"ConnectionName": connection_name}
    response = requests.get(f"http://{spider_url}/spider/allvm", params=params).json()

    not_registered_list = response["AllList"]["OnlyCSPList"]

    only_csp_list = []
    for vm in not_registered_list:
        name_id = vm["NameId"]
        system_id = vm["SystemId"]
        vm_dto = VmDto(name_id, system_id)
        only_csp_list.append(vm_dto)

    return only_csp_list


if __name__ == '__main__':
    app.run(debug=True)
