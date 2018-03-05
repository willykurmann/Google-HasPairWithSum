from unsorted_version import has_pair_with_sum

def test_data_vector_doesnt_contain_pair_with_sum():
    data = [1,2,3,9]
    sum = 8
    assert has_pair_with_sum(data,sum) == False

def test_data_vector_does_contain_pair_with_sum():
    data = [1,2,4,4]
    sum = 8
    assert has_pair_with_sum(data,sum) == True

def test_unsorted_data_vector():
    data = [4,4,1,2]
    sum = 8
    assert has_pair_with_sum(data,sum) == True