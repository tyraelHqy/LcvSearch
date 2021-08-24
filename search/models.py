from elasticsearch_dsl import DocType, Date, Completion, Keyword, Text
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalysis

connections.create_connection(hosts=["localhost"])


class CustomAnalyzer(_CustomAnalysis):
    def get_analysis_definition(self):
        return {}


ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])


class QAType(DocType):
    # QA类型
    suggest = Completion(analyzer=ik_analyzer)
    question = Text(analyzer="ik_max_word")
    create_date = Date()
    answer = Text(analyzer="ik_max_word")
    url = Keyword()
    environment = Keyword()

    class Meta:
        index = "qa_robot"
        doc_type = "qa_robot"


if __name__ == "__main__":
    QAType.init()
