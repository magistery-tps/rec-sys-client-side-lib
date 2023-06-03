#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------
import sys
sys.path.append('./src')
from recsys.domain_context import DomainContext
#------------------------------------------------------------------------------
#
#
#
#
#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
if __name__ == '__main__':
    DomainContext() \
        .bert_item_distance_matrix_job('multi-qa-mpnet-base-dot-v1') \
        .execute()
#------------------------------------------------------------------------------