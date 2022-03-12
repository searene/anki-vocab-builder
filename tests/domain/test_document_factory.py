import unittest

from tests.utils import get_test_session, get_test_vocab_builder_db
from vocab_builder.domain.document.Document import Document
from vocab_builder.domain.document.DocumentFactory import DocumentFactory


class DocumentFactoryTestCase(unittest.TestCase):

    def test_should_get_documents_after_creating_them(self):
        db = get_test_vocab_builder_db()
        Document.init_database(db)
        document_factory = DocumentFactory(db)

        document1 = document_factory.create_new_document("test_document_name_1", "test_document_contents_1")
        document2 = document_factory.create_new_document("test_document_name_2", "test_document_contents_2")

        document_list = document_factory.get_document_list()

        self.assertEqual(len(document_list), 2)
        self.assertEqual(document_list[0], document1)
        self.assertEqual(document_list[1], document2)


if __name__ == '__main__':
    unittest.main()
