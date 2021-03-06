# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: Mcl_Cmd_SidLookup_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.technique
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.survey.cmd.sidlookup', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.survey.cmd.sidlookup.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.survey.cmd.sidlookup.Params()
    tgtParams.id = lpParams['number']
    tgtParams.type = lpParams['type']
    tgtParams.local = lpParams['local']
    if lpParams['name'] != None:
        tgtParams.name = lpParams['name']
    rpc = mca.survey.cmd.sidlookup.tasking.RPC_INFO_QUERY
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        print 'res=%08x' % res
        mcl.tasking.RecordModuleError(res, 0, mca.survey.cmd.sidlookup.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)