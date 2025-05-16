import sqlite3
from contextlib import contextmanager

class Database:
    def __init__(self, db_path='resumes.db'):
        self.db_path = db_path
        self._init_db()
    
    @contextmanager
    def _get_connection(self):
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
        finally:
            conn.close()
    
    def _init_db(self):
        with self._get_connection() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS resumes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT,
                    phone TEXT,
                    skills TEXT,
                    experience TEXT,
                    education TEXT,
                    raw_text TEXT,
                    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
    
    def save_resume(self, resume_data):
        with self._get_connection() as conn:
            conn.execute('''
                INSERT INTO resumes (name, email, phone, skills, experience, education, raw_text)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                resume_data['name'],
                resume_data['contact_info']['email'],
                resume_data['contact_info']['phone'],
                ','.join(resume_data['skills']),
                '|'.join(resume_data['experience']),
                '|'.join(resume_data['education']),
                resume_data['raw_text']
            ))
    
    def get_resumes_by_skills(self, skills):
        with self._get_connection() as conn:
            query = '''
                SELECT id, name, email, phone, skills, experience, education, raw_text
                FROM resumes
            '''
            
            if skills and skills[0]:
                # Build a LIKE clause for each skill
                like_clauses = []
                params = []
                for skill in skills:
                    like_clauses.append('skills LIKE ?')
                    params.append(f'%{skill}%')
                
                query += ' WHERE ' + ' OR '.join(like_clauses)
            
            cursor = conn.execute(query, params)
            
            resumes = []
            for row in cursor.fetchall():
                resumes.append({
                    'id': row[0],
                    'name': row[1],
                    'email': row[2],
                    'phone': row[3],
                    'skills': row[4].split(','),
                    'experience': row[5].split('|') if row[5] else [],
                    'education': row[6].split('|') if row[6] else [],
                    'raw_text': row[7]
                })
            
            return resumes