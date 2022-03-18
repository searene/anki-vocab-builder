from typing import Optional

import vocab_builder.domain.word.Word
from vocab_builder.domain.word.Word import Word
from vocab_builder.domain.word.WordStatus import WordStatus
from vocab_builder.infrastructure import VocabBuilderDB


def __get_next_unknown_word(doc_id: int, offset: int, db: VocabBuilderDB) -> Optional[Word]:
    word_query_res = db.fetch_one(f"""
    select w.* from words w
    left join global_word_status g on w.text = g.word
    where g.word is null
        and w.skipped = 0
        and w.document_id = {doc_id}
    limit {offset}, 1
    """)
    if word_query_res is None:
        return None
    return vocab_builder.domain.word.Word.convert_word_data_object_to_word(word_query_res)


def get_next_word(doc_id: int, offset: int, word_status: WordStatus, db: VocabBuilderDB) -> Optional[Word]:
    if word_status == WordStatus.UNKNOWN:
        return __get_next_unknown_word(doc_id, offset, db)
    else:
        pass