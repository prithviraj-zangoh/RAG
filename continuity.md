# Day 4 LangChain + LangGraph RAG Project Continuity Document

## Background

I am completing a Day 4 LangChain + LangGraph RAG internship project.

The official guide requires:

* Git/GitHub workflow
* Docker/Compose
* Database/vector store
* LangChain
* LangGraph
* RAG pipeline
* Citations
* Evaluation checklist

I did NOT complete Day 3 (vector database workflow), so the learning path was adjusted to first teach the missing vector database concepts before building the actual project.

---

# Learning Style Requirements

When continuing:

* Assume I am a beginner.
* Avoid excessive repetition.
* Avoid re-explaining concepts already covered unless needed.
* Continue incrementally.
* Explain WHY each file exists.
* Explain WHY each piece of code exists.
* Do not dump a complete project at once.
* Build and verify one component at a time.
* If response length becomes a problem, stop naturally and continue in the next message instead of compressing explanations.

---

# Environment Information

Operating System:
Mac

Python:
Already installed and working

API Provider:
Groq

Environment Variable:

GROQ_API_KEY=<configured>

Project Folder:

day4-rag-project/

Folder Structure:

app/
data/
docs/
scripts/
tests/

requirements.txt
.env
.gitignore

---

# Phase A Completed

Completed:

* Python verification
* Git verification
* Docker verification
* Virtual environment setup
* requirements.txt
* package installation
* .env setup
* Git initialization
* Feature branch creation
* Initial commit

---

# Phase B Completed (Missing Day 3 Knowledge)

Topics learned:

## RAG Fundamentals

RAG = Retrieval Augmented Generation

Flow:

Question
↓
Retrieve Context
↓
Attach Context
↓
Generate Answer

---

## Embeddings

Learned that:

Text
↓
Embedding Model
↓
Vector

Example:

"I love dogs"

becomes

[0.11, 0.42, ...]

Vectors represent semantic meaning.

---

## Semantic Search

Experimented with:

SentenceTransformer

Model:

all-MiniLM-L6-v2

Compared:

"Employees receive 20 paid vacation days annually."

vs

"How many vacation days do employees get?"

using cosine similarity.

Learned that semantic similarity works even when wording changes.

---

## Mini Retrieval Demo

Built:

experiments/retrieval_demo.py

Implemented:

* document embeddings
* question embedding
* cosine similarity
* nearest document retrieval

Learned how vector search works internally.

---

## Chroma Theory

Learned:

Why vector databases exist.

Without Chroma:

Compare against every vector.

With Chroma:

Efficient nearest-neighbor search.

---

# Phase C Progress

## Data Created

Files inside data/

employee_handbook.txt

Contents:

Employees receive 20 paid vacation days annually.

Unused vacation days cannot be carried over into the next calendar year.

Employees must submit leave requests through the HR portal.

---

remote_work_policy.txt

Contents:

Employees may work remotely up to three days per week.

Remote employees must attend all scheduled team meetings.

Managers may require office attendance for important business activities.

---

security_policy.txt

Contents:

Employees must wear identification cards at all times while inside company premises.

Lost identification cards must be reported immediately.

Visitors must be escorted by an employee.

---

## Loader Created

File:

app/loaders.py

Purpose:

Load text files into LangChain Document objects.

Concept learned:

File
↓
Document Object

---

## Splitting Learned

Used:

RecursiveCharacterTextSplitter

Learned:

* chunk_size
* chunk_overlap
* why chunking exists
* why retrieval searches chunks instead of entire documents

---

## Embeddings Learned

Used:

sentence-transformers

Model:

all-MiniLM-L6-v2

Learned:

Chunks
↓
Embeddings
↓
Vectors

---

## Chroma Installed

Installed:

chromadb

Used local embeddings instead of OpenAI embeddings.

Reason:

No OpenAI API key.

Using Groq for generation.

Using local embedding model for retrieval.

---

## Vector Store Built

File:

app/vectorstore.py

Contains Chroma configuration.

Purpose:

Single source of truth for vector database setup.

---

## Ingestion Built

File:

scripts/ingest.py

Current responsibility:

Documents
↓
Load
↓
Split
↓
Embed
↓
Store in Chroma

Learned:

Ingestion = Load + Split + Embed + Store

Not just file loading.

---

## Chroma Database Created

Folder generated:

chroma_db/

Contains:

* chunks
* embeddings
* metadata
* indexes

Verified that chunks were stored.

---

## Retriever Built

File:

app/retriever.py

Uses:

similarity_search()

and later:

similarity_search_with_score()

Learned:

Question
↓
Embedding
↓
Vector Search
↓
Top Chunks

---

## Context Validation

File:

app/context_grader.py

Simple implementation:

Check best retrieval score.

Purpose:

Prevent generation when retrieval quality is poor.

Learned:

Vector databases always return something.

Need validation before generation.

---

## Groq Setup Completed

Installed:

langchain-groq

Verified:

test_groq.py

Worked successfully.

Model currently planned:

llama-3.3-70b-versatile

---

## Generator Built

File:

app/generator.py

Uses:

ChatGroq

Prompt:

* Answer ONLY using supplied context.
* If answer is unavailable:
  "I do not know based on the provided documents."

Learned:

Retriever finds facts.

LLM writes answers.

---

## End-to-End RAG Test Built

File:

test_rag.py

Current flow:

Question
↓
Retrieve
↓
Context
↓
Groq
↓
Answer

Result:

Basic RAG pipeline works.

---

# Current Understanding

I understand:

Documents
↓
Chunks
↓
Embeddings
↓
Vectors
↓
Chroma
↓
Retrieval
↓
Context Validation
↓
LLM
↓
Answer

---

# What Has NOT Been Built Yet

The next phase should start here.

Need to build:

## LangGraph

Required graph:

START
↓
Retrieve
↓
Grade Context
↓
Generate Answer
↓
Format Response
↓
END

Need detailed explanation of:

* Graph state
* Nodes
* Edges
* Conditional routing
* Compilation
* Invocation

Need to understand WHY LangGraph is needed versus normal functions.

---

After LangGraph:

Need to build:

* app/main.py
* citations
* answer formatting
* fallback behavior
* evaluation checklist
* README
* Dockerfile
* compose.yaml
* testing workflow
* GitHub issue / PR workflow
* final deliverables
* acceptance criteria verification

---

# Instruction For Continuation

Continue from:

"Phase C — LangGraph Implementation"

Do not restart from RAG fundamentals.

Assume all prior phases are completed successfully.
