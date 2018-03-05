from unsorted_version import has_pair_with_sum

''' Should test the data vector doesnt contain a pair that adds up to the sum
'''
def test_data_vector_doesnt_contain_pair_with_sum():
    data = [1,2,3,9]
    sum = 8
    assert has_pair_with_sum(data,sum) == False

''' Should test the data vector does contain a pair that adds up to the sum
'''
def test_data_vector_does_contain_pair_with_sum():
    data = [1,2,4,4]
    sum = 8
    assert has_pair_with_sum(data,sum) == True
