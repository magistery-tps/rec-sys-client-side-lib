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
    DomainContext().nmf_distance_matrix_job.execute()
#------------------------------------------------------------------------------