import os
import pytest
import shutil
from sqe import enhance_docs
from unittest.mock import patch

# ##### find info after string
# # TODO use @pytest.fixtures and test more?
# def test_find_info_after_string_green():
#     search_for = "foo"
#     expected = "bar"
#     extract_from = "foo: bar"
#     assert expected == enhance_docs.find_info_after_string(search_for, extract_from)
#
# def test_find_info_after_string_green_extra():
#     search_for = "foo"
#     expected = "bar"
#     extract_from = "blahblah\nfoo: bar\nblahblah"
#     assert expected == enhance_docs.find_info_after_string(search_for, extract_from)
#
# def test_find_info_after_string_not_in():
#     search_for = "nope"
#     expected = "bar"
#     extract_from = "blahblah\nfoo: bar\nblahblah"
#     with pytest.raises(Exception):
#         enhance_docs.find_info_after_string(search_for, extract_from)
#
# #####
# TARGET_KEY = "target file"
# PROMPT_KEY = "prompt"
# #
# # def read_and_rewrite(target_file, user_prompt):
# #     with open(target_file, "r") as target:
# #         base_document = target.read_lines()
# #
# #     prompt = "Given <PROMPT>{user_prompt}</PROMPT>, return an edited version of the following text. <DOC>{base_document}</DOC>"
# #
# #     response = openai.Completion.create(
# #         engine=ENGINE,
# #         prompt=prompt,
# #         max_tokens=500
# #     )
# #     with open(target_file, "w") as target:
# #         target.write(response.choices[0].text.strip())
# #
#
def test_read_and_rewrite_response_clobbers_file(mock_ai):
    expected = "fit, sit, kit"
    mock_ai.return_value.choices[0].text.strip.return_value = expected
    # copy fixture
    target_file = "todotmp/poem.txt"
    # TODO rm
    try:
        os.mkdir("todotmp")
    except FileExistsError:
        pass
    fixture_file = "tests/fixtures/poem.txt"
    shutil.copyfile(fixture_file, target_file)

    # rewrite
    enhance_docs.read_and_rewrite(target_file, "make it rhyme")

    # read new and assert
    with open(target_file, "r") as target:
        actual = target.read()

    assert expected == actual

##### sanity
# def test_sanity():
#     assert False
