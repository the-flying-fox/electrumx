# Copyright (c) 2019, Neil Booth
#
# All rights reserved.
#
# See the file "LICENCE" for information about the copyright
# and warranty status of this software.


class TxIndex:

    def __init__(self):
        pass

    def tx_hash_to_num(self, tx_hash):
        '''Looks up a tx_hash.  Returns None if not found, otherwise it returns the txnum of the
        hash.
        '''
        pass

    def tx_num_to_hash(self, tx_num):
        '''Looks up a tx_num.  Returns its tx_hash (32 bytes).'''
        pass

    def update(self, tx_gen):
        '''Update the transaction index for transactions yielded by tx_gen.'''
        pass

    def backup_to(self, tx_num):
        '''Back up so that tx numbers from and including tx_num are invalidated.'''
        pass
