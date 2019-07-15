# ANSIBLE API 2.4

## 需求1：实现Ansible全局变量
### 1. 首先，分析变量可存放的位置。
#### 1.1. 多重变量定义，Ansible变量支持多重变量，通常从如下4个位置检索。
1. Inventory配置文件（默认/etc/ansible/hosts）
2. Playbook中vars定义的区域
3. Roles中vars目录下的文件
4. Roles同级目录group_vars和host_vars目录下的文件

#### 1.2. 其他Inventory参数列表。
这些变量是ansible内置的，列举如下：  
ansible_ssh_host  
ansible_ssh_user  
ansible_ssh_private_key_file

#### 1.3. Playbook变量
在使用ansible-playbook执行时，可以使用--extra-vars指定额外的变量或调用文件中的变量。  
ansible-playbook example.yml --extra-vars "foo=bar"  
ansible-playbook example.yml --extra-vars "@even_more_vars.json"  
ansible-playbook example.yml --extra-vars "@even_more_vars.yml"


### 2. 其次，变量优先级，由高到低的排序。
1. 在命令行中定义的变量，也就是使用-e定义的变量。
2. 在Inventory中定义的连接变量，如ansible_ssh_user。
3. 大多数的其他变量，如命令行转换，play的变量，included的变量，role中的变量等。
4. 在Inventory定义的其他变量。
5. 由系统通过gather_facts方法发现的facts。
6. "Role默认变量"，这个默认的值，很容易丧失优先权。


### 3. 再之，现状。
ansible服务器上已经写好了很多roles，然后一个单独一playbook去执行。


### 4. 最后，总结。
1. 可以实现，就是把roles同级目录的group_vars下的all做成web化即可。