using UnityEngine;

public class PipeSpawner : MonoBehaviour // (구 MakePipe)
{
    [Header("난이도별 장애물 리스트")]
    public GameObject[] easyPipes;   // 0~10점용 (가만히 있는 파이프)
    public GameObject[] hardPipes;   // 10점 이상용 (움직이거나 회전하는 파이프)

    public float timeDiff;
    float timer = 0;

    void Update()
    {
        if (!GameManager.gameStarted) return;

        timer += Time.deltaTime;
        if (timer > timeDiff)
        {
            SpawnPipe();
            timer = 0;
        }
    }

    void SpawnPipe()
    {
        GameObject prefabToSpawn;
        int currentScore = ScoreManager.Instance.getScore();

        // 점수에 따라 생성할 배열 선택
        if (currentScore < 10)
        {
            // 쉬운 파이프 중 랜덤 하나 선택
            int randomIndex = Random.Range(0, easyPipes.Length);
            prefabToSpawn = easyPipes[randomIndex];
        }
        else
        {
            // 어려운 파이프 중 랜덤 하나 선택
            int randomIndex = Random.Range(0, hardPipes.Length);
            prefabToSpawn = hardPipes[randomIndex];
        }

        // 생성 및 위치 설정
        GameObject newPipe = Instantiate(prefabToSpawn);
        newPipe.transform.position = new Vector3(3.2f, Random.Range(-2.3f, 2.3f), 0);

        // 5초 뒤 삭제 (ObjectMover 스크립트가 파이프에 붙어있어야 왼쪽으로 감)
        Destroy(newPipe, 5.0f);
    }
}