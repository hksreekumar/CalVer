from cCalVer import CalVerYYYYMM
from datetime import datetime

def test_CalVerYYYYMM_getTagPreText():
    # arrange
    my_versioner = CalVerYYYYMM()
    # act
    pre_test = my_versioner.getTagPreText()
    pre_test_splitted = pre_test.split('.')
    # assert
    assert pre_test_splitted[0] == str(datetime.now().year)[2:]
    assert pre_test_splitted[1] == str(datetime.now().month).zfill(2)

def test_CalVerYYYYMM_addLastPatch():
    # arrange
    my_versioner = CalVerYYYYMM()
    # (a) act and assert
    new_tag = my_versioner.addLastPatch('23.01',[],'master') # no existing tags
    assert new_tag == '23.01.1'
    # (b) act and assert
    new_tag = my_versioner.addLastPatch('23.01',['23.01.1','23.01.2'],'master') # there are existing tags
    assert new_tag == '23.01.3'
    # (c) act and assert
    new_tag = my_versioner.addLastPatch('23.01',['23.01.4','23.01.10'],'master') # there are existing tags - but mixed
    assert new_tag == '23.01.11'
    # (d) act and assert
    new_tag = my_versioner.addLastPatch('23.01',['23.01.4','23.01.10'],'main') # a main branch
    assert new_tag == '23.01.11'
    # (e) act and assert
    new_tag = my_versioner.addLastPatch('23.01',['23.01.4','23.01.10'],'beta') # a beta branch
    assert new_tag == '23.01.11-beta'
    # (f) act and assert - I am in beta and developed a new beta function
    new_tag = my_versioner.addLastPatch('23.01',['23.01.4'],'beta') 
    assert new_tag == '23.01.5-beta'
    # (g) act and assert - Continuing (f) I am now changing to master branch and make a release
    new_tag = my_versioner.addLastPatch('23.01',['23.01.4','23.01.5-beta'],'master') 
    assert new_tag == '23.01.5'
    # (h) act and assert - Now change to a new branch again
    new_tag = my_versioner.addLastPatch('23.01',['23.01.4','23.01.5-beta','23.01.5'],'alpha-doc') 
    assert new_tag == '23.01.6-alpha-doc'
    # (i) act and assert - Now change to the beta again
    new_tag = my_versioner.addLastPatch('23.01',['23.01.4','23.01.5-beta','23.01.5','23.01.6-alpha-doc'],'beta') 
    assert new_tag == '23.01.6-beta'
    # (j) act and assert - Now change to the master again
    new_tag = my_versioner.addLastPatch('23.01',['23.01.4','23.01.5-beta','23.01.5','23.01.6-alpha-doc','23.01.6-beta'],'master') 
    assert new_tag == '23.01.6'
    # (k) act and assert - Now change to the master after two months
    new_tag = my_versioner.addLastPatch('23.03',['23.01.4','23.01.5-beta','23.01.5','23.01.6-alpha-doc','23.01.6-beta'],'master') 
    assert new_tag == '23.03.1'
    # (l) act and assert - Develop on different branches on same month and merge to master on the same month
    new_tag = my_versioner.addLastPatch('23.01',['23.01.2-alpha-doc','23.01.2-beta','23.01.1'],'master') 
    assert new_tag == '23.01.2'
    # (l) act and assert - Develop on different branches on same month and merge to master on a different month
    new_tag = my_versioner.addLastPatch('23.02',['23.01.2-alpha-doc','23.01.2-beta','23.01.1'],'master') 
    assert new_tag == '23.02.1'


