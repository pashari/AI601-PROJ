CREATE TABLE IF NOT EXISTS predictions (
  id SERIAL PRIMARY KEY,
  title TEXT,
  content TEXT,
  predicted_label TEXT,
  predicted_sentiment TEXT,
  persons JSONB,
  organizations JSONB,
  locations JSONB
);

INSERT INTO predictions (title, content, predicted_label, predicted_sentiment, persons, organizations, locations)
VALUES 
('وزیر اعظم کا دورہ چین', 'وزیر اعظم نے چین کا دورہ کیا جس میں معاشی معاہدے ہوئے۔', 'Politics', 'Positive', '["وزیر اعظم"]', '["حکومت پاکستان"]', '["چین"]'),
('کرکٹ میں فتح', 'پاکستان نے بھارت کو ورلڈ کپ میں شکست دے دی۔', 'Sports', 'Positive', '["بابر اعظم"]', '["پی سی بی"]', '["پاکستان", "بھارت"]');
