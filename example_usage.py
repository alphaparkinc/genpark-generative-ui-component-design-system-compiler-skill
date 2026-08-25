from client import GenerativeUiComponentDesignSystemCompilerClient

def main():
    client = GenerativeUiComponentDesignSystemCompilerClient()
    res = client.compile_generative_react_component('Multi-tenant billing tier checkout table with annual discount toggle')
    print('Component ID: ' + res['component_id'] + ' (' + res['design_system'] + ')')
    print('Size: ' + str(res['tsx_code_length_bytes']) + ' bytes | ARIA Compliant: ' + str(res['accessible_aria_labels_included']))
    print('Preview: ' + res['live_react_sandbox_url'] + ' | NPX Ready: ' + str(res['copy_paste_npx_ready']))

if __name__ == '__main__':
    main()
