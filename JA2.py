

import citrix.sdk  # or import citrix.automation


# Connect to the Citrix environment

citrix_client = citrix.sdk.Client()  # or citrix.automation.Client()

citrix_client.connect(url='http://globegatepmx/Citrix/Web/', username='yuktal', password='Amdocs@2023')


# Enumerate available resources

resources = citrix_client.get_resources()  # or citrix_client.enumerate_resources()


# Launch an RDP session

selected_resource = resources[0]  # Select a resource from the list

rdp_session = selected_resource.launch_rdp()  # or citrix_client.launch_rdp(selected_resource)


# Additional steps to handle the RDP session, such as connecting to it or interacting with it

# ...


# Disconnect from the Citrix environment

citrix_client.disconnect()





