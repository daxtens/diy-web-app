import boto.ec2
import boto.route53, boto.route53.record
import time
machines = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
            'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twentyone', 'twentytwo',
            'twentythree', 'twentyfour', 'twentyfive', 'twentysix', 'twentyseven', 'twentyeight', 'twentynine', 'thirty']

def spawn(name, ec2conn, ami):
    reservation = ec2conn.run_instances(ami, key_name=name, instance_type='t1.micro', security_groups=['ssh-https'])
    machine = reservation.instances[0]
    machine.add_tag('Name', name)
    while machine.public_dns_name == '':
        time.sleep(5)
        machine.update()
    print(machine.public_dns_name)
    records = boto.route53.record.ResourceRecordSets(route53conn, 'Z1K1CSURKSBWDX')
    change = records.add_change("CREATE", name+".compcon.dja.id.au", "CNAME")
    change.add_value(machine.public_dns_name)
    records.commit()

def destroy(name, ec2conn):
    reservations = ec2conn.get_all_instances()
    machines = [x.instances[0] for x in reservations if x.instances[0].key_name == name]
    if not machines:
        print("%s not found." % name)
        return
    machines[0].terminate()
    records = route53conn.get_all_rrsets('Z1K1CSURKSBWDX')
    change = records.add_change("DELETE", name+".compcon.dja.id.au.", "CNAME")
    change.add_value([x.to_print() for x in records if x.name == name+".compcon.dja.id.au."][0])
    records.commit()    



# do stuff!
syd_ec2conn = boto.ec2.connect_to_region("ap-southeast-2")
singapore_ec2conn = boto.ec2.connect_to_region("ap-southeast-1")
route53conn = boto.connect_route53()
syd_ami = 'ami-04ea7a3e'
singapore_ami = 'ami-64084736' 
# spawn 1-15 
[spawn(name, syd_ec2conn, syd_ami) for name in machines[0:15]]
# spawn 16-30 
[spawn(name, singapore_ec2conn, singapore_ami) for name in machines[15:]]
# destroy 1-15 [destroy(name, syd_ec2conn) for name in machines[0:15]]
# destroy 16-30 [destroy(name, singapore_ec2conn) for name in machines[15:]]
