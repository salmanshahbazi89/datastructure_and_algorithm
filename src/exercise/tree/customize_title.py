from src.basic_data_structures.MyTree import TreeNode

if __name__ == '__main__':
    ceo = TreeNode({'name': 'Nilupul', 'designation': 'CEO'})

    # CTO Hierarchy

    cto = TreeNode({'name': 'Chinmay', 'designation': 'CTO'})
    infra_head = TreeNode({'name': 'Vishwa', 'designation': 'Infrastructure Head'})
    cloud_manager = TreeNode({'name': 'Dhaval', 'designation': 'Cloud Manager'})
    app_manager = TreeNode({'name': 'Abhijit', 'designation': 'App Manager'})
    infra_head.add_child(cloud_manager)
    infra_head.add_child(app_manager)
    app_head = TreeNode({'name': 'Aamir', 'designation': 'Application Head'})
    cto.add_child(infra_head)
    cto.add_child(app_head)

    hr = TreeNode({'name': 'Gels', 'designation': 'HR Head'})
    recruitment_manager = TreeNode({'name': 'Peter', 'designation': 'Recruitment Manager'})
    policy_manager = TreeNode({'name': 'Waqas', 'designation': 'Policy Manager'})
    hr.add_child(recruitment_manager)
    hr.add_child(policy_manager)

    ceo.add_child(cto)
    ceo.add_child(hr)

    ceo.print_tree('name')
    ceo.print_tree('designation')
    ceo.print_tree('both')
