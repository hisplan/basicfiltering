'''
@Description : This tool helps to test VarDict 
@Created :  03/23/2017
@Updated : 03/23/2017
@author : Ronak H Shah

'''

import filecmp
import os
from subprocess import Popen
import shlex
import nose
from nose.tools import with_setup

def setup_function(): 
    pass
 
def teardown_function():
    pass
 
@with_setup(setup_function, teardown_function)
def main():
    this_dir, this_filename = os.path.split(__file__)
    new_dir = os.path.dirname(this_dir)
    inputFileVcf = os.path.join(new_dir, "data", "sample_input", "PoolTumor2-T_bc52_VarDict_1.4.6.vcf")
    outFileVcf = os.path.join(new_dir, "PoolTumor2-T_bc52_VarDict_1.4.6_STDfilter.vcf")
    outFileTxt = os.path.join(new_dir, "PoolTumor2-T_bc52_VarDict_1.4.6_STDfilter.txt")
    cmpFileVcf = os.path.join(new_dir, "data", "sample_output", "PoolTumor2-T_bc52_VarDict_1.4.6_STDfilter.vcf")
    cmpFileTxt = os.path.join(new_dir, "data", "sample_output", "PoolTumor2-T_bc52_VarDict_1.4.6_STDfilter.txt")
    scriptFile = os.path.join(new_dir, "filter_vardict.py")
    cmd = "python " + scriptFile + " -tsn PoolTumor2-T " + "-ivcf " + inputFileVcf
    args = shlex.split(cmd)
    if(os.path.isfile(outFileTxt) or (os.path.isfile(outFileVcf))):
        os.remove(outFileTxt)
        os.remove(outFileVcf)
    else:
        proc = Popen(args)
        proc.wait()
        retcode = proc.returncode
        if(retcode >= 0):
            code = 1
        else:
            assert 0
        try:
            assert filecmp.cmp(outFileTxt, cmpFileTxt)
        except AssertionError:
            print "The file " + outFileTxt + " and " + cmpFileTxt + " are not the same"
            pytest.raiseError()  
        try:
            assert filecmp.cmp(outFileVcf, cmpFileVcf)
        except AssertionError:
            print "The file " + outFileVcf + " and " + cmpFileVcf + " are not the same"
            pytest.raiseError()  

if __name__ == '__main__':
    nose.main()
