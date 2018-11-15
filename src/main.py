import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import config
from processing.preprocessing import excel_to_df
from searches.exact_search import find_exact_matches, count_exact_matches


def main():
    file_name = config.CROPS['file_name']
    data_df = excel_to_df(file_name)
    term = sys.argv[1] # get_term()
    match_df = find_exact_matches(term, data_df)
    print(count_exact_matches(term, match_df), match_df)


if  __name__ =='__main__':
    main()
