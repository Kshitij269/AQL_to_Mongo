# File: generate_mock_data.py

from pymongo import MongoClient
from faker import Faker
import random

fake = Faker()
client = MongoClient("mongodb://localhost:27017")
db = client["ehr_db"]
collection = db["ehr"]

def generate_record(extension_id):
    return {
        "subjectOfCare": {
            "extension": extension_id
        },
        "Composition": {
            "content": {
                "items": {
                    "parts": {
                        "at0000": {
                            "parts": {
                                "at0001": {
                                    "value": {
                                        "originalText": {
                                            "value": fake.sentence(nb_words=3)
                                        }
                                    }
                                },
                                "at0002": {
                                    "value": {
                                        "magnitude": random.randint(100, 150)
                                    }
                                },
                                "at0003": {
                                    "value": {
                                        "defining_code": {
                                            "code_string": str(random.randint(60, 90))
                                        }
                                    }
                                },
                                "at0004": {
                                    "value": {
                                        "defining_code": {
                                            "code_string": str(round(random.uniform(36.5, 38.5), 1))
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "context": {
            "start_time": {
                "value": fake.date_time_this_year().isoformat()
            },
            "location": fake.city(),
            "setting": {
                "defining_code": {
                    "code_string": random.choice(["home", "ambulatory", "emergency"])
                }
            },
            "health_care_facility": {
                "name": fake.company()
            },
            "participations": {
                "at0005": {
                    "function": {
                        "value": random.choice(["nurse", "physician", "technician"])
                    }
                }
            },
            "other_context": {
                "items": {
                    "at0001": {
                        "items": {
                            "at0002": {
                                "value": {
                                    "value": random.choice(["Observation", "Triage", "Examination"])
                                }
                            }
                        }
                    }
                }
            }
        }
    }

mock_records = [generate_record(f"ANON_SERV_RSC:{str(fake.random_number(digits=10))}") for _ in range(20)]

collection.insert_many(mock_records)
print("✅ Inserted 20 mock EHR records into MongoDB!")
